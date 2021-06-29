# -*- coding: gbk -*-
from define import *
from common.log import LogError
import queue
from common import ssh
import functools
import traceback
import windowmessage
import threading

class CSrvOptManager(object):
	def __init__(self):
		self.m_Srv2Handler = {}
	
	def AddOpt(self, ip, opt, *args, callback=None):
		if ip not in self.m_Srv2Handler:
			self.m_Srv2Handler[ip] = CSrvOptHandler(ip)
			t=threading.Thread(target=self.m_Srv2Handler[ip].Run)
			t.start()
		
		self.m_Srv2Handler[ip].Enqueue(opt, *args, callback=callback)
	
	def EndManager(self):
		for handler in self.m_Srv2Handler.values():
			handler.End()

class CSrvOptHandler(object):
	def __init__(self, ip):
		self.m_ip = ip
		self.m_RunFlag = True
		self.m_queue = queue.Queue()
	
	def Enqueue(self, opt, *args, callback=None):
		self.m_queue.put((opt, args, callback))
	
	def End(self):
		self.m_RunFlag = False
	
	def Run(self):
		from ui import popup
		while self.m_RunFlag:
			try:
				try:
					opt, args, callback = self.m_queue.get(timeout=5)
				except queue.Empty:
					pass
				else:
					if not self.m_RunFlag:
						break
					
					client = ssh.GetSshClient(self.m_ip)
					if not client:
						windowmessage.g_MsgHandler.PutFunc(functools.partial(popup.showerror, 'error', '%s连接不上'%self.m_ip))
						continue
					
					client.DoRun(opt, args, callback)
					
			except Exception as e:
				windowmessage.g_MsgHandler.PutFunc(functools.partial(popup.scroll_text, ['在%s执行%s报错' % (self.m_ip, OPT_NAME.get(opt, opt)), repr(e)]))
				LogError("server handler unexpected error:" + repr(e) + traceback.format_exc())

if 'g_OptManager' not in globals().keys():
	g_OptManager = CSrvOptManager()

