# -*- coding: gbk -*-

from tkinter import *
from tkinter import ttk
from common.log import LogError
import functools
import windowoperate
import windowmessage
import re
import traceback
from tkinter import simpledialog
from game.gameconfig import *
from game.serverprocs import *
from ui import popup

DEFAULT_MAKEPY_COMB_VALUE 	= {'查询(excel列表)': 'query', '导所有表格': 'server' }
CONFIG_GREATE	= 1

BASE_INFO_TYPE		= 1
BASE_INFO_STATE		= 2
BASE_INFO_MEMORY	= 3
BASE_INFO_IP		= 4
BASE_INFO = {
	BASE_INFO_IP		: "IP:",
	BASE_INFO_TYPE		: "类型:",
	BASE_INFO_STATE		: "状态:",	#未启动/桃手/九州/运行中/主控/战斗服
	BASE_INFO_MEMORY	: "内存:",
}

def _separator_blank(parent, pixel=8, side='top', **kwargs):
	if side in ('top', 'bottom'):
		sep = Frame(parent, height=pixel, **kwargs)
		sep.pack_propagate(0)
		sep.pack(side=side, fill='x')
	else:
		sep = Frame(parent, width=pixel, **kwargs)
		sep.pack_propagate(0)
		sep.pack(side=side, fill='y')

def _spearator_line(parent, hori=True):
	if hori:
		ttk.Separator(parent, orient='horizontal').pack(fill='x')
	else:
		ttk.Separator(parent, orient='vertical').pack(side='left', fill='y')

class PageFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		
		self.select_server_frame = SelectFrame(self)	#服务器列表页面
		self.server_frame = ServerFrame(self)	#某服务器详情页面
		self.server_frame.pack_forget()
		self.select_server_frame.pack(expand='yes', fill='both')
	
	def Show(self):
		self.server_frame.pack_forget()
		self.select_server_frame.pack(expand='yes', fill='both')
	
	def Hide(self):
		if self.server_frame.isshow:
			self.server_frame.Hide()
	
	def SelectServer(self, ip):
		if self.server_frame.isshow and self.server_frame.ip == ip:
			return
		self.select_server_frame.pack_forget()
		self.server_frame.Show(ip)
		self.server_frame.pack(expand='yes', fill='both')
		
	def ReturnBack(self):
		self.server_frame.Hide()
		self.server_frame.pack_forget()
		self.select_server_frame.pack(expand='yes', fill='both')
		
class SelectFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		canvas = Canvas(self, scrollregion=(0,0,0,47*(len(serverlist.SERVER_DATA)/4+1 + len(serverlist.SERVER_DATA_CLASSIFIED))))
		canvas.pack(expand='yes', fill='both')
		vbar = Scrollbar(canvas, orient=VERTICAL)  # 竖直滚动条
		vbar.pack(side='right', fill='y')
		vbar.configure(command=canvas.yview)
		
		body = Frame(canvas)
		body.pack(expand='yes', fill='both')
		
		canvas.config(yscrollcommand=vbar.set)  # 设置
		canvas.create_window((185, 420), window=body)  # 起始坐标点
		
		usertps = GetUserTypeSeq()
		for tp in usertps:
			Label(body, text=USERTYPE_NAME[tp]+":", font=entry_font, height=2, anchor='w').pack(expand='yes', fill='x')
			
			f = Frame(body)
			f.pack(expand='yes', fill='x')
			
			ips = serverlist.SERVER_DATA_CLASSIFIED[tp]
			for j, ip in enumerate(ips):
				b = Button(f, text=serverlist.GetServerName(ip), bd=2, bg='skyblue', font = 'bold', command=functools.partial(self.master.SelectServer, ip),  width=9)
				b.grid(row=j//4, column=j%4)
			
			col_count, row_count = f.grid_size()
			for col in range(col_count):
				f.grid_columnconfigure(col, minsize=90)
			
			for row in range(row_count):
				f.grid_rowconfigure(row, minsize=40)

class ServerFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.isshow = False
		self.ip = 0
		self.srvname = StringVar()
	
		body = self
		title = Frame(body)
		title.pack(fill='x')
		Button(title, text='<--返回', font='bold', command=self.master.ReturnBack).pack(side='left')
		Label(title, textvariable=self.srvname, width=26, font=('楷体', 18, 'bold')).pack(side='left')
		_separator_blank(body)
		_spearator_line(body)
		_separator_blank(body)
		
		self.baseinfo_frame = BaseInfoFrame(body)
		self.baseinfo_frame.pack(fill='x')
		
		canvas = Canvas(self, scrollregion=(0, 0, 0, 500))
		canvas.pack(expand='yes', fill='both')
		vbar = Scrollbar(canvas, orient=VERTICAL)  # 竖直滚动条
		vbar.pack(side='right', fill='y')
		vbar.configure(command=canvas.yview)
		body = Frame(canvas, width=405, height=500)
		body.pack_propagate(0)
		body.pack(expand='yes', fill='both')
		canvas.config(yscrollcommand=vbar.set)  # 设置
		canvas.create_window((200, 248), window=body)  # 起始坐标点
		
		self.operation_frame = OperationFrame(body)
		self.operation_frame.pack(fill='x')
	
	def Show(self, ip):
		self.isshow = True
		self.ip = ip
		self.srvname.set("%s(%s)" %(serverlist.GetServerName(ip), USERTYPE_NAME[serverlist.SERVER_DATA[ip]["user_type"]]))
		self.Refresh()
	
	def Refresh(self):
		self.RefreshLockStatus()
		self.baseinfo_frame.RefreshStateInfo(self.ip)
		self.operation_frame.OperationRefresh(self.ip)
	
	def RefreshTrace(self, ip):
		if self.isshow and self.ip == ip:
			self.operation_frame.RefreshTraceStatus()
	
	def RefreshMakepy(self, ip):
		if self.isshow and self.ip == ip:
			self.operation_frame.RefreshMakepyCmd()
	
	def DoServerConfig(self, ip, opt, output_str, operate):
		if self.isshow and self.ip == ip:
			self.operation_frame.ServerConfig(operate, opt, output_str)
	
	def RefreshLockStatus(self):
		pass

	def Hide(self):
		self.isshow = False

class BaseInfoFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.init()
	
	def init(self):
		self.ip = 0
		self.contents = []
		self.properties = {}
		self.proc_running = {}	#进程代号： 正在运行的进程昵称
	
	def refresh_severinfo(self):
		self.properties[BASE_INFO_IP][1]['text'] = self.ip
		self.properties[BASE_INFO_TYPE][1]['text'] = '；'.join([SERVERTYPE_2_NAME[tp] for tp in serverlist.SERVER_DATA[self.ip]["srv_type"]])
		windowoperate.g_OptManager.AddOpt(self.ip, OPT_QUERY_MEMERY, callback=functools.partial(self.refresh_memory, self.ip))
		
		procs = GetServerProcs(self.ip)
		for i, (idx, proc, note) in enumerate(procs):
			windowoperate.g_OptManager.AddOpt(self.ip, OPT_QUERY_PROCS, proc, callback=functools.partial(self.refresh_proc_state, self.ip, idx, i == len(procs)-1))
			if note == "switchto":
				windowoperate.g_OptManager.AddOpt(self.ip, OPT_QUERY_SWITCH, callback=functools.partial(self.refresh_proc_name, self.ip, idx, ))
	
	def operate_refresh_severinfo(self):
		from ui import mainframe
		self.proc_running = {}
		self.properties[BASE_INFO_STATE][1]['text'] = ''
		self.refresh_severinfo()
		
		if serverlist.SERVER_DATA[self.ip]["user_type"] is USERTYPE_DEVELOPER:	#开发服才显示 url路径
			mainframe.g_MsgWin.AddPage(self.ip)
			mainframe.g_MsgWin.ChangePage(self.ip)
			procs = GetServerProcs(self.ip)
			for idx, proc, note in procs:
				opt = PROC_CODE_QUERY.get(idx)
				if opt is not None:
					windowoperate.g_OptManager.AddOpt(self.ip, OPT_QUERY_CODE_INFO, opt, callback=functools.partial(self.output_code_info, self.ip, idx))
		
	def output_code_info(self, ip, idx, result):
		from ui import mainframe
		if self.ip != ip:
			return
		
		d = []
		codepath, revision, timestr = [None] * 3
		for line in result.split('\n'):
			if line.startswith("URL:"):
				codepath = line[4:].strip()
			elif line.startswith("最后修改的版本:"):
				revision = line[len("最后修改的版本:"):].strip()
			elif line.startswith("最后修改的时间:"):
				timestr = line[len("最后修改的时间:"):].strip()[:10]
			if codepath and revision and timestr:
				d.append([codepath, revision, timestr])
				codepath, revision, timestr = [None] * 3
		
		s1 = ""
		for i, (codepath, revision, timestr) in enumerate(d):
			if i == 0:
				s1 += "%s:\n"%PROC_NICKNAME[idx]
			s1 += "\tSVN路径：%s\n\t当前版本号：%s\n\t当前版本号时间：%s\n\n"%(codepath, revision, timestr)
		if s1:
			mainframe.g_MsgWin.AppendConsoleMessage(ip, s1)
	
	def refresh_proc_name(self, ip, idx, result):
		if self.ip != ip:
			return
			
		if idx in self.proc_running:
			result = result.strip()
			new_procname = "九州" if result in ["os_jiuzhou", "os_aquarius"] else "桃手" if result in ["os_taoshou", "os_pisces"] else PROC_NICKNAME[idx]
			self.proc_running[idx] = new_procname
			self.properties[BASE_INFO_STATE][1]['text'] = '；'.join([name + "运行中" for name in self.proc_running.values()]) if self.proc_running else "未启动"
	
	def refresh_memory(self, ip, result):
		if self.ip != ip:
			return
		try:
			self.properties[BASE_INFO_MEMORY][1]['text'] = "%d M" % int(result.strip())
		except:
			pass
	
	def refresh_proc_state(self, ip, idx, final, result):
		if self.ip != ip:
			return
		try:
			if int(result.strip()):
				self.proc_running[idx] = PROC_NICKNAME[idx]
		except:
			pass
			
		if final:
			self.properties[BASE_INFO_STATE][1]['text'] = '；'.join([name + "运行中" for name in self.proc_running.values()]) if self.proc_running else "未启动"
		
	def RefreshStateInfo(self, ip):
		if ip != self.ip:
			for ctrl in self.contents:
				ctrl.destroy()
			self.init()
			self.ip = ip
			
			f = Frame(self)
			f.pack(fill="x")
			self.contents.append(f)
			Label(f, text='基本信息:', font=entry_font, anchor='w').pack(side='left')
			Button(f, text="刷新", bd=2, font=('', 11), command=self.operate_refresh_severinfo).pack(side='left', padx=3, pady=3)
			
			f1 = Frame(self)
			f1.pack(fill="x")
			self.contents.append(f1)
			
			lst = [
				[BASE_INFO_IP, BASE_INFO_MEMORY],
				[BASE_INFO_TYPE],
				[BASE_INFO_STATE],
			]
			for idxs in lst:
				f2 = Frame(f1)
				f2.pack(fill='x')
				for i, idx in enumerate(idxs):
					f3 = Frame(f2)
					f3.grid(row=0, column=i, sticky=W)
					lb1 = Label(f3, text=BASE_INFO[idx], font=('仿宋', 11, 'normal'), )
					lb1.pack(side='left')
					lb2 = Label(f3)
					lb2.pack(side='left')
					self.properties[idx] = [lb1, lb2]
					
			f3 = Frame(self)
			self.contents.append(f3)
			f3.pack(fill="x")
			_separator_blank(f3)
			_spearator_line(f3)
			_separator_blank(f3)
			self.refresh_severinfo()

class OperationFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.init()
	
	def init(self):
		self.ip = 0
		self.contents = []
		self.opt_2_tracebutton = {}
		self.makepy_comb = None
		self.m_config_frame = None
		self.selfdefine_history_idx = {}
		
	def OperationRefresh(self, ip):
		if self.ip != ip:
			for ctrl in self.contents:
				ctrl.destroy()
			self.init()
			self.ip = ip
			opnames = GetSrvOpts(ip)
			
			for i, lb in enumerate(sorted(opnames.keys())):
				f = Frame(self)
				self.contents.append(f)
				f.pack(fill='x')
				if i != 0:
					_separator_blank(f)
				Label(f, text=OPTLABEL_NAME[lb], font=entry_font, ).pack(side='left')
				
				opts_by_lb = opnames[lb]
				for opts in opts_by_lb:
					f = Frame(self)
					self.contents.append(f)
					f.pack(fill='x')
					for opt in opts:
						opname = OPT_BUTTON_NAME.get(opt, OPT_NAME.get(opt))
						if opt in [OPT_LABEL_CENTER, OPT_LABEL_BATTLE]:
							Label(f, text=opname, ).pack(side='left')
						elif opt in [OPT_SHELL_SYSTEM_CMD, OPT_SELF_DEFINE_SUDO]:
							Label(f, text=opname, width=18).pack(side='left')
							entry = Entry(f, width=30, highlightthickness=1)
							entry.pack(side='left', padx=3, pady=3)
							entry.bind('<Return>', functools.partial(self.operate_selfdefine_command, opt))
							entry.bind('<Up>', functools.partial(self.show_selfdefine_history, opt, 0))
							entry.bind('<Down>', functools.partial(self.show_selfdefine_history, opt, 1))
						elif opt is OPT_BATCH_OPT_SET:
							Label(f, text=opname, width=12).pack(side='left')
							c = ttk.Combobox(f, width=14, state='readonly', value=BATCH_SET_DATA,)
							c.set(BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]))
							c.pack(side='left', padx=3, pady=3)
							c.bind('<<ComboboxSelected>>', self.operate_batchset)
						elif opt is OPT_MAKEPY:
							self.makepy_comb = ttk.Combobox(f, width=30)
							self.makepy_comb.pack(side='left', padx=3, pady=10)
							self.makepy_comb['value'] = list(DEFAULT_MAKEPY_COMB_VALUE.keys()) + list(MAKEPY_CMD_DATA.get(self.ip, {}).keys())
							self.makepy_comb.current(0)
							b = Button(f, text=opname, bd=2, font=('', 11), command=functools.partial(self.operate_makepy, opt))
							b.pack(side='left', padx=3, pady=3)
						elif opt in GAMECONFIG_CMD_2_QUERY.keys():
							b = Button(f, text=opname, bd=2, font=('', 11), command=functools.partial(self.operate_gameconfig, opt))
							b.pack(side='left', padx=3, pady=3)
						elif opt in FORCEUPDATE_NEED_PARAMETER_CMDS:
							b = Button(f, text=opname, bd=2, font=('', 11), command=functools.partial(self.operate_forceupdate_para, opt))
							b.pack(side='left', padx=3, pady=3)
						elif opt in DEBUG_2_GAMECONFIG:
							b = Button(f, text=opname, bd=2, font=('', 11), command=functools.partial(self.operate_debug, opt))
							b.pack(side='left', padx=3, pady=3)
						else:
							b = Button(f, text=opname, bd=2, font=('', 11), command=functools.partial(self.operate, opt))
							b.pack(side='left', padx=3, pady=3)#padx设置外边距
							if opt in TRACE_CMDS:
								self.opt_2_tracebutton[opt] = b
							if opt in UPDATE_REVISION_CMDS:
								b.bind('<Button-3>', functools.partial(self.operate_update_revision, opt))
							if opt in SHOWLOG_CMDS:
								b.bind('<Button-3>', functools.partial(self.operate_log, opt))
			f2 = Frame(self)
			self.contents.append(f2)
			f2.pack(fill="x")
			_separator_blank(f2)
			_spearator_line(f2)
			_separator_blank(f2)
		
		self.RefreshTraceStatus()
		self.RefreshLockStatus()

	def RefreshTraceStatus(self):
		from common import ssh
		opts = ssh.GetTracingOpts(self.ip)
		for opt, bt in self.opt_2_tracebutton.items():
			if opt in opts:
				bt['text'] = '停止追踪'
				bt['bg'] = 'skyblue'
			else:
				bt['text'] = OPT_BUTTON_NAME.get(opt, OPT_NAME.get(opt))
				bt['bg'] = 'SystemButtonFace'
	
	def RefreshMakepyCmd(self):
		if self.makepy_comb:
			self.makepy_comb['value'] = list(DEFAULT_MAKEPY_COMB_VALUE.keys()) + list(MAKEPY_CMD_DATA.get(self.ip, {}).keys())

	def RefreshLockStatus(self):
		pass
	
	def operate_batchset(self, event):
		value = event.widget.get()
		BATCH_CONFIG_DATA[self.ip] = value
		with open(BATCH_CONFIG_FILE, 'w') as f:
			json.dump(BATCH_CONFIG_DATA, f, indent=8, ensure_ascii=False)
	
	def show_selfdefine_history(self, opt, dir, event):
		historylst = SELFDEFINE_HISTORY_DATA.get(str(opt), {}).get(self.ip, [])
		idx = self.selfdefine_history_idx.get(opt, {}).get(self.ip, 0)
		n = len(historylst)
		
		if dir == 0:#往上
			idx -= 1
		elif dir == 1:#往下
			idx += 1
		if -n <= idx < 0:
			self.selfdefine_history_idx.setdefault(opt, {})[self.ip] = idx
			event.widget.delete(0, 'end')
			event.widget.insert(0, historylst[idx])
	
	def operate_selfdefine_command(self, opt, event):
		from ui import mainframe
		mainframe.g_MsgWin.AddPage(self.ip)
		mainframe.g_MsgWin.ChangePage(self.ip)

		msg = event.widget.get().strip()
		if msg:
			windowoperate.g_OptManager.AddOpt(self.ip, opt, msg)
			historylst = SELFDEFINE_HISTORY_DATA.setdefault(str(opt), {}).setdefault(self.ip, [])
			historylst.append(msg)
			if len(historylst) > MAX_HISTORY_CNT:
				SELFDEFINE_HISTORY_DATA[str(opt)][self.ip] = historylst[len(historylst)-MAX_HISTORY_CNT: ]
			WriteJsonFile(SELFDEFINE_CMD_HISTORY_FILE, SELFDEFINE_HISTORY_DATA)
	
	def operate_makepy(self, opt):
		from ui import mainframe
		mainframe.g_MsgWin.AddPage(self.ip)
		mainframe.g_MsgWin.ChangePage(self.ip)
		
		if self.makepy_comb:
			make_str = self.makepy_comb.get().strip()
			d = {}
			d.update(DEFAULT_MAKEPY_COMB_VALUE)
			d.update(MAKEPY_CMD_DATA.get(self.ip, {}))
			make_str = d.get(make_str, make_str)
			if len(make_str) == 0:
				make_str = 'query'
			windowoperate.g_OptManager.AddOpt(self.ip, opt, make_str, callback=functools.partial(makepy_callback, self.ip, make_str))
	
	def operate_forceupdate_para(self, opt):
		from ui import mainframe
		if opt is OPT_FORCEUPDATE_KUAFU_JZ:
			para = simpledialog.askstring('九州强更', '请输入svn路径：（点击[基本信息]的刷新按钮可显示当前使用的svn路径）', parent=mainframe.g_App)
		elif opt is OPT_FORCEUPDATE_KUAFU_PISCES:
			para = simpledialog.askstring('桃手强更', '请输入svn路径：（点击[基本信息]的刷新按钮可显示当前使用的svn路径）', parent=mainframe.g_App)
		else:
			para = simpledialog.askstring('强更', '请输入svn路径：', parent=mainframe.g_App)
		if para and para.strip():
			mainframe.g_MsgWin.AddPage(self.ip)
			mainframe.g_MsgWin.ChangePage(self.ip)
			windowoperate.g_OptManager.AddOpt(self.ip, opt, para.strip())
	
	def operate_gameconfig(self, opt):
		from ui import mainframe
		mainframe.g_MsgWin.AddPage(self.ip)
		mainframe.g_MsgWin.ChangePage(self.ip)
		
		def query_gameconfig_callback(output_str):
			windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_App.pages['服务器'].server_frame.DoServerConfig, self.ip, opt, output_str, CONFIG_GREATE))
		
		query_opt = GAMECONFIG_CMD_2_QUERY[opt]
		windowoperate.g_OptManager.AddOpt(self.ip, query_opt, callback=query_gameconfig_callback)
	
	def ServerConfig(self, operate, opt, output_str):
		if operate == CONFIG_GREATE:
			self.create_config_frame(opt, output_str)
	
	def CloseConfig(self, ip):
		if ip == self.ip and self.m_config_frame:
			self.m_config_frame.destroy()
			self.m_config_frame = None
	
	def create_config_frame(self, opt, rawdata):
		from ui import configframe
		if self.m_config_frame:
			self.m_config_frame.destroy()
			self.m_config_frame = None
		
		configfile = serverlist.SERVER_DATA[self.ip].get("configfile", {}).get(opt, DEFAULT_GAMECONFIG_FILE[opt])
		try:
			if not rawdata:
				windowmessage.g_MsgHandler.PutFunc(functools.partial(popup.scroll_text, ["该服配置文件 %s 内容为空" % configfile, ], "获取debug端口失败"))
				return
			cfgdata = CConfigData(rawdata)
		except Exception as e:
			popup.scroll_text(["该服配置文件 %s 有语法错误，请按提示先手动修正" % configfile, repr(e)], "%s error"%configfile)
			return
		
		self.m_config_frame = configframe.ConfigPopup(self.ip, opt, cfgdata)
		self.m_config_frame.setpos((60, 100))
		self.m_config_frame.display()
	
	def operate_log(self, opt, event):
		from ui import mainframe
		
		logfile = simpledialog.askstring(OPT_NAME.get(opt), '请输入文件名(不带后缀)', parent=mainframe.g_App)
		if logfile:
			mainframe.g_MsgWin.AddPage(self.ip)
			mainframe.g_MsgWin.ChangePage(self.ip)
			windowoperate.g_OptManager.AddOpt(self.ip, opt, logfile)
	
	def operate_update_revision(self, opt, event):
		from ui import mainframe
		from ui import popup
		
		revision = simpledialog.askstring(OPT_NAME.get(opt), '请输入版本号：', parent=mainframe.g_App)
		if revision:
			try:
				revision = int(revision.strip())
			except:
				popup.showerror('代码版本号 error', '请填入正确的整数')
				return
			
			mainframe.g_MsgWin.AddPage(self.ip)
			mainframe.g_MsgWin.ChangePage(self.ip)
			windowoperate.g_OptManager.AddOpt(self.ip, opt, revision)
	
	def operate_debug(self, opt):
		config_opt = DEBUG_2_GAMECONFIG[opt]
		query_opt = GAMECONFIG_CMD_2_QUERY[config_opt]
		windowoperate.g_OptManager.AddOpt(self.ip, query_opt, callback=functools.partial(self.open_telnet_debug, self.ip, opt, config_opt))
	
	def open_telnet_debug(self, ip, opt, config_opt, configdata):
		from ui import mainframe
		configfile = serverlist.SERVER_DATA[ip].get("configfile", {}).get(config_opt, DEFAULT_GAMECONFIG_FILE[config_opt])
		try:
			if not configdata:
				windowmessage.g_MsgHandler.PutFunc(functools.partial(popup.scroll_text, ["该服配置文件 %s 内容为空" % configfile, ], "获取debug端口失败"))
				return
			cfgobj = CConfigData(configdata)
		except Exception as e:
			windowmessage.g_MsgHandler.PutFunc(functools.partial(popup.scroll_text, ["该服配置文件 %s 有语法错误，请按提示先手动修正" % configfile, repr(e)], "获取debug端口失败"))
			return
		
		debugport = cfgobj.Get("debug")
		mainframe.g_MsgWin.AddPage(ip, opt)
		mainframe.g_MsgWin.ChangePage(ip, opt)
		windowoperate.g_OptManager.AddOpt(ip, opt, debugport)
	
	def operate(self, opt):
		from ui import mainframe
		if opt in [OPT_FORCEUPDATE, ]:
			optname = OPT_BUTTON_NAME.get(opt, OPT_NAME.get(opt))
			if not popup.double_confirm(optname, '你确定要%s吗'%optname):
				return
		
		mainframe.g_MsgWin.AddPage(self.ip)
		mainframe.g_MsgWin.ChangePage(self.ip)
		if opt is OPT_DATE:
			def date_callback(ip, default_time):
				windowmessage.g_MsgHandler.PutFunc(functools.partial(changetime, default_time, ip))
			windowoperate.g_OptManager.AddOpt(self.ip, OPT_DATE_QUERY, callback=functools.partial(date_callback, self.ip))
		else:
			windowoperate.g_OptManager.AddOpt(self.ip, opt)

def GetSrvOpts(ip):
	user_type = serverlist.SERVER_DATA[ip]["user_type"]
	srv_type = serverlist.SERVER_DATA[ip]["srv_type"]
	srv_opts = serverlist.SERVER_DATA[ip].get("srv_opts", [])
	
	if srv_opts:
		opnames = srv_opts
	else:
		opnames = {
			OPTLABEL_DEFAULT: [
				[OPT_DATE_QUERY, OPT_DATE, ],
				[OPT_UPDATECODE, OPT_REBOOTGAME, OPT_SHOWLOG, OPT_TRACELOG],
				[OPT_FORCEUPDATE, OPT_UPDATE_MAP, OPT_GAMECONFIG, OPT_DEBUG],
				[OPT_SHELL_SYSTEM_CMD, ],
				[OPT_SELF_DEFINE_SUDO, ],
			],
		}
	
		if user_type is USERTYPE_DEVELOPER:
			if SERVERTYPE_GAME in srv_type:  # 开发服的游戏服
				opnames = {
					OPTLABEL_JZ: [
						[OPT_UPDATE_JZ, OPT_REBOOT_JZ, OPT_SHOWLOG_JZ, OPT_TRACELOG_JZ, OPT_GAMECONFIG_JZ, OPT_DEBUG_JZ],
					],
					OPTLABEL_PISCES: [
						[OPT_UPDATE_PISCES, OPT_REBOOT_PISCES, OPT_SHOWLOG_PISCES, OPT_TRACELOG_PISCES, OPT_GAMECONFIG_PISCES, OPT_DEBUG_PISCES],
					],
					OPTLABEL_COMMON: [
						[OPT_DATE_QUERY, OPT_DATE],
						[OPT_SHELL_SYSTEM_CMD, ],
						[OPT_SELF_DEFINE_SUDO, ],
						[OPT_BATCH_OPT_SET],
					],
				}
		elif user_type in [USERTYPE_CEHUA_PISCES, USERTYPE_CEHUA_YUJIAN_JIUZHOU]:	#策划服
			opnames = {
				OPTLABEL_DEFAULT: [
					[OPT_DATE_QUERY, OPT_DATE, ],
					[OPT_UPDATECODE, OPT_REBOOTGAME, OPT_SHOWLOG, OPT_TRACELOG],
					[OPT_FORCEUPDATE, OPT_UPDATE_MAP, OPT_GAMECONFIG, OPT_DEBUG],
					[OPT_MAKEPY,],
					[OPT_SHELL_SYSTEM_CMD, ],
					[OPT_SELF_DEFINE_SUDO, ],
				],
			}
		if SERVERTYPE_KUAFU in srv_type:	#跨服
			if user_type is USERTYPE_DEVELOPER:
				opnames = {
					OPTLABEL_JZ: [
						[OPT_FORCEUPDATE_KUAFU_JZ],
						[OPT_LABEL_CENTER, OPT_UPDATE_CENTER_JZ, OPT_REBOOT_CENTER_JZ, OPT_SHOWLOG_CENTER_JZ, OPT_TRACELOG_CENTER_JZ, OPT_GAMECONFIG_CENTER_JZ, OPT_DEBUG_CENTER_JZ],
						[OPT_LABEL_BATTLE, OPT_UPDATE_BATTLE_JZ, OPT_REBOOT_BATTLE_JZ, OPT_SHOWLOG_BATTLE_JZ, OPT_TRACELOG_BATTLE_JZ, OPT_GAMECONFIG_BATTLE_JZ, OPT_DEBUG_BATTLE_JZ],
					],
					OPTLABEL_PISCES: [
						[OPT_FORCEUPDATE_KUAFU_PISCES],
						[OPT_LABEL_CENTER, OPT_UPDATE_CENTER_PISCES, OPT_REBOOT_CENTER_PISCES, OPT_SHOWLOG_CENTER_PISCES, OPT_TRACELOG_CENTER_PISCES, OPT_GAMECONFIG_CENTER_PISCES, OPT_DEBUG_CENTER_PISCES],
						[OPT_LABEL_BATTLE, OPT_UPDATE_BATTLE_PISCES, OPT_REBOOT_BATTLE_PISCES, OPT_SHOWLOG_BATTLE_PISCES, OPT_TRACELOG_BATTLE_PISCES, OPT_GAMECONFIG_BATTLE_PISCES, OPT_DEBUG_BATTLE_PISCES],
					],
					OPTLABEL_COMMON: [
						[OPT_DATE_QUERY, OPT_DATE, ],
						[OPT_SHELL_SYSTEM_CMD, ],
						[OPT_SELF_DEFINE_SUDO, ],
						[OPT_BATCH_OPT_SET],
					],
				}
			else:
				opnames = {
					OPTLABEL_DEFAULT: [
						[OPT_DATE_QUERY, OPT_DATE, ],
						[OPT_LABEL_CENTER, OPT_UPDATE_CENTER, OPT_REBOOT_CENTER, OPT_SHOWLOG_CENTER, OPT_TRACELOG_CENTER, OPT_GAMECONFIG_CENTER, OPT_DEBUG_CENTER],
						[OPT_LABEL_BATTLE, OPT_UPDATE_BATTLE, OPT_REBOOT_BATTLE, OPT_SHOWLOG_BATTLE, OPT_TRACELOG_BATTLE, OPT_GAMECONFIG_BATTLE, OPT_DEBUG_BATTLE],
						[OPT_SHELL_SYSTEM_CMD, ],
						[OPT_SELF_DEFINE_SUDO, ],
					],
				}
		
		if SERVERTYPE_AUTH in srv_type:
			auth_opts = {
				OPTLABEL_AUTH: [
					[OPT_UPDATE_AUTH, OPT_REBOOT_AUTH, OPT_SHOWLOG_AUTH, OPT_SHOWLOG_REGISTER],
				],
			}
			opnames.update(auth_opts)
		if SERVERTYPE_DATASRV in srv_type:
			datasrv_opts = {
				OPTLABEL_DATASRV: [
					[OPT_UPDATE_DATASRV, OPT_REBOOT_DATASRV, OPT_SHOWLOG_DATASRV],
				],
			}
			opnames.update(datasrv_opts)
	return opnames

def changetime(default_time, ip):
	from ui import mainframe
	
	timestr = simpledialog.askstring('调时', '请输入时间（年-月-日 时:分:秒）', initialvalue=default_time, parent=mainframe.g_App)
	if timestr:
		windowoperate.g_OptManager.AddOpt(ip, OPT_DATE, timestr.strip())

def makepy_callback(ip, make_str, output_str):
	from ui import mainframe
	if make_str != 'query':
		return
	
	try:
		dct = {}
		lst = output_str.split('\n')
		for line in lst:
			if re.match('.+:\s*\w+', line):
				kv = line.split(':')
				if len(kv) != 2:
					continue
				k, v = kv
				dct[k.strip()] = v.strip()
		
		MAKEPY_CMD_DATA[ip] = dct
		with open(MAKEPY_CMD_FILE, 'w') as f:
			json.dump(MAKEPY_CMD_DATA, f, indent=8, ensure_ascii=False)
		windowmessage.g_MsgHandler.PutFunc(functools.partial(mainframe.g_App.pages['服务器'].server_frame.RefreshMakepy, ip))
	except Exception as e:
		LogError("makepy callback unexpected error:" + repr(e) + traceback.format_exc())
