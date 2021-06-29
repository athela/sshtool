# -*- coding: gbk -*-

from common.log import LogError
import traceback
import queue
from ui import mainframe
from define import *

class CMessageQueue(object):
	def __init__(self):
		self.m_queue = queue.Queue()
	
	def Put(self, element):
		self.m_queue.put(element)
	
	def PutFunc(self, element):
		self.m_queue.put(element)
	
	def Dequeue(self):
		try:
			msgdct = {}
			func = None
			while True:
				try:
					element = self.m_queue.get(block=False)
					if isinstance(element, tuple):
						ip, msg, second_scrolltext, win_opt = element
						key = (ip, win_opt, 1 if second_scrolltext else 0)
						msgdct.setdefault(key, "")
						msgdct[key] += msg
					else:
						func = element
						break
				except queue.Empty:
					break
			
			for (ip, win_opt, use_second_scrolltext), msg in msgdct.items():
				mainframe.g_MsgWin.AppendConsoleMessage(ip, msg, use_second_scrolltext, win_opt)
			
			if func:
				func()
		except Exception as e:
			LogError("message handler unexpected error:" + repr(e) + traceback.format_exc())

if 'g_MsgHandler' not in globals().keys():
	g_MsgHandler = CMessageQueue()
