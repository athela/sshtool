# -*- coding: gbk -*-

import paramiko
from paramiko_expect import SSHClientInteraction
from define import *
import time
import threading
import functools
import windowmessage
from game.command import *
from game import serverlist
from game import gameconfig
import telnetlib
import re

'''
	sudo -S -p ''：#用stdin的方式输入密码且提示语改为空串
		-S：	The -S (stdin) option causes sudo to read the password from the standard input instead of the terminal
			   device.  The password must be followed by a newline character.
		-p：	改变输入密码的提示语

	exec_command 参数environment={"encoding":'gbk'}解决了python2 stdout.read出来是乱码的问题
	python3则不需要，需在stdout.read()后解码

	tail 直接用exec_command会阻塞， https://blog.csdn.net/weixin_46059803/article/details/109307927
	切换用户，没用到 https://blog.csdn.net/hans99812345/article/details/111802340
'''

class CConnectClient(object):
	PORT	= 22
	def __init__(self, ip):
		global g_SshManager
		self.m_ip = ip
		self.m_ssh_fd = paramiko.SSHClient()
		self.m_ssh_fd.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.m_ssh_fd.connect(ip, username=SSH_USER, password=SSH_PASSWORD)
		self.m_trans_fd = None
		self.m_Opt2TailThread = {}	#支持一个服，有多个tail同时执行
		self.m_Opt2TelnetDebug = {}
		g_SshManager[ip] = self
	
	def IsAlive(self):
		trans = self.m_ssh_fd.get_transport()
		if trans and trans.is_active():
			return True
		else:
			return False
	
	def DoUploadFile(self, file, target_dir, override):
		try:
			self.m_trans_fd = paramiko.Transport(sock=(self.m_ip, self.PORT))
			self.m_trans_fd.connect(username=SSH_USER, password=SSH_PASSWORD)
			sftp = paramiko.SFTPClient.from_transport(self.m_trans_fd)
			
			try:
				sftp.stat(target_dir)
			except:
				stdin, stdout, stderr = self.m_ssh_fd.exec_command('mkdir -p %s' % target_dir)
				if stdout.channel.recv_exit_status() != 0:
					return False
			
			target_file = target_dir + file
			if override:
				sftp.put(file, target_file.encode('gbk'))
			else:
				try:
					sftp.stat(target_file.encode('gbk'))
				except:
					sftp.put(file, target_file.encode('gbk'))
				else:
					target_file = "%s_%s" % (target_file, time.strftime("%Y%m%d%H%M%S", time.localtime(int(time.time()))))
					sftp.put(file, target_file.encode('gbk'))
		except Exception as e:
			print(str(e))
			return False
		return True
	
	def DoGameConfig(self, opt, configobj, callback):
		StartOptMsg(self.m_ip, opt)
		datafile = configobj.GetFile()
		if self.DoUploadFile(datafile, UPLOAD_REMOTE_PATH, True):
			configfile = serverlist.SERVER_DATA[self.m_ip].get("configfile", {}).get(opt, gameconfig.DEFAULT_GAMECONFIG_FILE[opt])
			bakfile = UPLOAD_REMOTE_PATH + "%s_%s" % (configfile, time.strftime("%Y%m%d%H%M%S", time.localtime(int(time.time()))))
			cmd = 'cp %s %s; mv %s %s; cat %s' % (configfile, bakfile, UPLOAD_REMOTE_PATH+datafile, configfile, configfile)
			self.CommonExec(cmd, opt, callback=callback)
		EndOptMsg(self.m_ip, opt)
	
	def DoRun(self, opt, args, callback=None):
		if opt in DEBUG_2_GAMECONFIG:
			self.Telnet(opt, args[0])
		elif opt is OPT_DEBUG_WRITE:
			self.TelnetWrite(args[0], args[1])
		elif opt is OPT_CLOSE_PAGE:
			self.Close(args[0])
		elif opt in GAMECONFIG_CMD_2_QUERY:
			self.DoGameConfig(opt, args[0], callback)
		else:
			cmd, use_tail = GetCommandStr(self.m_ip, opt, args)
			
			if use_tail:
				self.TailExec(opt, cmd)
			else:
				StartOptMsg(self.m_ip, opt)
				if cmd is None:
					OutPut(self.m_ip, "%s指令不正确\n"%opt)
				else:
					if isinstance(cmd, list):
						for c in cmd:
							self.CommonExec(c, opt, callback)
					else:
						self.CommonExec(cmd, opt, callback)
				EndOptMsg(self.m_ip, opt)
	
	def CommonExec(self, cmd, opt, callback=None):
		stdin, stdout, stderr = self.m_ssh_fd.exec_command(cmd)
		stdin.write(SSH_PASSWORD + "\n")
		stdin.flush()
		
		result = stdout.read().decode("gbk", "replace")
		result += stderr.read().decode("gbk", "replace")
		if opt not in IGNORE_OUTPUT_COMMAND:
			OutPut(self.m_ip, result)
		if callback:
			callback(result)
	
	def StopTail(self, opt):
		from ui import mainframe
		
		self.m_Opt2TailThread[opt].StopFromUI()
		windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_App.pages['服务器'].server_frame.RefreshTrace, self.m_ip))
	
	def StartTail(self, opt, cmd):
		from ui import mainframe
		
		if opt in FORCEUPDATE_CMDS + [OPT_MAKEPY]:
			cls = CForceupdateOpt
			use_second_scrolledtext = False
		else:
			cls = CTailOpt
			use_second_scrolledtext = True if self.m_Opt2TailThread and all(t.m_use_second_scrolledtext is False for t in self.m_Opt2TailThread.values()) else False
		tail_obj = cls(self, cmd, opt, use_second_scrolledtext)
		th = threading.Thread(target=tail_obj.Run)
		th.start()
		windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_App.pages['服务器'].server_frame.RefreshTrace, self.m_ip))
	
	def TelnetWrite(self, debugopt, msg):
		telnetobj = self.m_Opt2TelnetDebug.get(debugopt)
		if telnetobj:
			telnetobj.Write(msg)
	
	def Telnet(self, opt, debugport):
		self.CloseTelnet(opt)
		self.m_Opt2TelnetDebug[opt] = CTelnet(self.m_ip, opt, debugport)
		th = threading.Thread(target=self.m_Opt2TelnetDebug[opt].Run)
		th.start()
	
	def CloseTelnet(self, opt=None):
		if opt is None:
			for telobj in self.m_Opt2TelnetDebug.values():
				if telobj and telobj.m_RunFlag is True:
					telobj.StopTelnet()
			self.m_Opt2TelnetDebug = {}
		else:
			telobj = self.m_Opt2TelnetDebug.get(opt)
			if telobj and telobj.m_RunFlag is True:
				telobj.StopTelnet()
				del self.m_Opt2TelnetDebug[opt]
	
	def TailExec(self, opt, cmd):
		if opt in self.m_Opt2TailThread:
			self.StopTail(opt)
		else:
			self.StartTail(opt, cmd)
	
	def StopAllTail(self):
		for opt in list(self.m_Opt2TailThread.keys()):
			self.StopTail(opt)
	
	def CloseSsh(self):
		g_SshManager.pop(self.m_ip)
		self.StopAllTail()
		self.m_ssh_fd.close()
		if self.m_trans_fd:
			self.m_trans_fd.close()
	
	def Close(self, opt=None):
		if opt is None:
			self.CloseSsh()
			self.CloseTelnet()
		elif opt is OPT_SSH_WINDOW:
			self.CloseSsh()
		else:
			self.CloseTelnet(opt)

class CTelnet(object):
	def __init__(self, ip, opt, port):
		self.m_ip = ip
		self.m_port = port
		self.m_RunFlag = None
		self.m_tn = None
		self.m_opt = opt
	
	def StopTelnet(self):
		self.m_RunFlag = False
		if self.m_tn:
			self.m_tn.close()
			self.m_tn = None
	
	def Write(self, msg):
		msg = msg + "\n"
		msg = msg.encode('gbk')
		self.m_tn.write(msg)
	
	def InvalidState(self, msg):
		from ui import mainframe
		OutPutDebug(self.m_ip, self.m_opt, msg)
		windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_MsgWin.RefreshDebugState, self.m_ip, self.m_opt, True))
	
	def Run(self):
		OutPutDebug(self.m_ip, self.m_opt, "连接 %s Debug端口%s\n" % (self.m_ip, self.m_port))
		try:
			self.m_tn = telnetlib.Telnet(self.m_ip, self.m_port)
			self.m_RunFlag = True
		except ConnectionRefusedError as e:
			self.InvalidState(str(e)+'\n')
			return
		except:
			self.InvalidState("Debug连接失败\n")
			return
		
		try:
			while self.m_RunFlag:
				msg = self.m_tn.read_eager()
				msg = msg.decode('gbk', "replace")
				if msg:
					OutPutDebug(self.m_ip, self.m_opt, msg)
		except Exception as e:
			self.StopTelnet()
			self.InvalidState("Debug连接断开\n")

class CTailOpt(object):
	def __init__(self, parent, cmd, opt, use_second_scrolledtext):
		from ui import mainframe
		self.m_Parent = parent
		self.m_ip = self.m_Parent.m_ip
		self.m_Cmd = cmd
		self.m_opt = opt
		self.m_StopFlag = False
		self.m_use_second_scrolledtext = use_second_scrolledtext
		if self.m_use_second_scrolledtext:
			windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_MsgWin.AddSecondScrolledText, self.m_ip))
		self.m_Parent.m_Opt2TailThread[self.m_opt] = self
	
	def StopFromUI(self):
		self.Stop()
	
	def Stop(self):
		from ui import mainframe
		self.m_Parent.m_Opt2TailThread.pop(self.m_opt)
		EndOptMsg(self.m_ip, self.m_opt, self.m_use_second_scrolledtext)
		if self.m_use_second_scrolledtext:
			windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_MsgWin.RemoveSecondScrolledText, self.m_ip))
		self.m_StopFlag = True
		self.m_Parent = None
	
	def stop_interact(self, outputline):
		return self.m_StopFlag
	
	def Run(self):
		StartOptMsg(self.m_ip, self.m_opt, self.m_use_second_scrolledtext)
		prompt = '.*$.*'
		SSHClientInteraction.tail = tail
		interact = SSHClientInteraction(self.m_Parent.m_ssh_fd, encoding='gbk', display=True)
		
		interact.send('\n')
		interact.expect(prompt)
		
		interact.send(self.m_Cmd)
		interact.expect(TRACE_PROMPT)
		
		interact.send(SSH_PASSWORD+'\n')
		output_func = OutPut2 if self.m_use_second_scrolledtext else OutPut
		interact.tail(timeout=3, output_callback=functools.partial(output_func, self.m_ip), stop_callback=self.stop_interact)  # 阻塞

class CForceupdateOpt(CTailOpt):
	def __init__(self, parent, cmd, opt, use_second_scrolledtext):
		super(CForceupdateOpt, self).__init__(parent, cmd, opt, use_second_scrolledtext)
		self.m_target_num = 2 if opt in FORCEUPDATE_TWO_PATH_CMDS else 1
		self.m_end_line_num = 0
		self.m_end_suffix = re.compile('over') if opt is OPT_MAKEPY else re.compile("取出版本 \d+。")
	
	def StopFromUI(self):
		pass
	
	def stop_interact(self, outputline):
		if self.m_end_suffix.match(outputline):
			self.m_end_line_num += 1
			if self.m_end_line_num == self.m_target_num and not self.m_StopFlag:
				self.Stop()
		return self.m_StopFlag

def tail(self, line_prefix=None, callback=None, output_callback=None, stop_callback=lambda x: False, timeout=None):
	import struct,socket
	output_callback = output_callback if output_callback else self.output_callback
	timeout = timeout if timeout else 2 ** (struct.Struct(str('i')).size * 8 - 1) - 1
	self.channel.settimeout(timeout)
	current_line = b''
	line_counter = 0
	line_feed_byte = '\n'.encode(self.encoding)
	while True:
		if stop_callback(""):			#添加的部分, tail照抄 SSHClientInteraction.tail源码
			break
		try:
			buffer = self.channel.recv(1)
		except socket.timeout:
			continue
		
		if len(buffer) == 0:
			break
		
		if stop_callback(""):
			break
		
		current_line += buffer
		
		if buffer == line_feed_byte:
			current_line_decoded = current_line.decode(self.encoding)
			if line_counter:
				if callback:
					output_callback(callback(line_prefix, current_line_decoded))
				else:
					if line_prefix:
						output_callback(line_prefix)
					output_callback(current_line_decoded)
			if stop_callback(current_line_decoded):
				break
			line_counter += 1
			current_line = b''

def OutPut(ip, msg):
	windowmessage.g_MsgHandler.Put((ip, msg, False, OPT_SSH_WINDOW))

def OutPut2(ip, msg):
	windowmessage.g_MsgHandler.Put((ip, msg, True, OPT_SSH_WINDOW))

def OutPutDebug(ip, opt, msg):
	windowmessage.g_MsgHandler.Put((ip, msg, False, opt))

def StartOptMsg(ip, opt, use_second_srolledtext=False):
	if opt not in OPT_NAME:
		return
	
	msg = "\n{:-^60}\n".format("开始["+OPT_NAME[opt]+"]" + time.strftime("[%m-%d %H:%M:%S] ", time.localtime(int(time.time()))))
	if use_second_srolledtext:
		OutPut2(ip, msg)
	else:
		OutPut(ip, msg)

def EndOptMsg(ip, opt, use_second_srolledtext=False):
	if opt not in OPT_NAME:
		return
	
	msg = "{:-^60}\n\n".format("结束["+OPT_NAME[opt]+"]" + time.strftime("[%m-%d %H:%M:%S] ", time.localtime(int(time.time()))))
	if use_second_srolledtext:
		OutPut2(ip, msg)
	else:
		OutPut(ip, msg)

def GetTracingOpts(ip):
	client = GetSshClient(ip, False)
	return client.m_Opt2TailThread.keys() if client else []

def GetSshClient(ip, create=True):
	client = g_SshManager.get(ip)
	if client:
		if client.IsAlive():
			return client
		else:
			client.Close()
	if create:
		try:
			return CConnectClient(ip)
		except:
			pass

def Clear():
	global g_SshManager
	for ip in list(g_SshManager.keys()):
		g_SshManager[ip].Close()
	WriteJsonFile(TELNET_HISTORY_FILE, TELNET_HISTORY_DATA)

if "g_SshManager" not in globals().keys():
	g_SshManager = {}
