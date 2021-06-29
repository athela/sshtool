# -*- coding: gbk -*-
from tkinter import *
from tkinter import scrolledtext
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
import time

class PageFrame(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.m_save_buttons = {}
		
		f = Frame(self, height=40)
		f.pack_propagate(0)
		f.pack(fill='x')
		Label(f, text="请输入IP列表进行批量操作(每个IP一行):", font=entry_font, height=1, anchor='w').pack(expand='yes', fill='x')
		
		f = Frame(self)
		f.pack(fill='x')
		left = Frame(f, width=280, height= 300)
		left.pack_propagate(0)
		left.pack(side='left')
		right = Frame(f, width=200, height=200)
		right.pack_propagate(0)
		right.pack(side='left')
		
		self.m_text = scrolledtext.ScrolledText(left, bd=3, )
		self.m_text.pack(expand='yes', fill='both')
		
		for row in range(8):
			n = row + 1
			bt1 = Button(right, text='保存%d' % n, bd=2, font=('仿宋', 12, 'normal'), command=functools.partial(self.save, n))
			bt1.grid(row=row, column=0, padx=3, pady=3)
			bt2 = Button(right, text='显示%d' % n, bd=2, font=('仿宋', 12, 'normal'), command=functools.partial(self.show_history, n))
			bt2.grid(row=row, column=1, padx=3, pady=3)
			if str(n) in BATCH_HISTORY_DATA:
				bt1['fg'] = 'blue'
				bt2['fg'] = 'blue'
			self.m_save_buttons[n] = [bt1, bt2]
		
		f = Frame(self)
		f.pack(fill='x')
		funcs = [self.DoDate, self.DoUpdateCode, self.DoRebootProc, self.DoTraceLog]
		names = ['一键调时', '一键更新', '一键重启', '一键跟踪日志']
		for name, func in dict(zip(names, funcs)).items():
			b = Button(f, text=name, bd=3, font=('微软雅黑', 12, 'normal'), command=func)
			b.pack(side='left', padx=6, pady=20)
			if name == '批量更新':
				b.bind('<Button-3>', self.DoUpdateCodeWithRevision)
		
		for opt in [OPT_SHELL_SYSTEM_CMD, OPT_SELF_DEFINE_SUDO]:
			f = Frame(self)
			f.pack(fill='x')
			opname = OPT_BUTTON_NAME[opt]
			Label(f, text=opname, width=18).pack(side='left')
			entry = Entry(f, width=30, highlightthickness=1)
			entry.pack(side='left', padx=3, pady=3)
			entry.bind('<Return>', functools.partial(self.DoSelfdefineCommand, opt))
			entry.bind('<Up>', functools.partial(self.show_selfdefine_history, opt, 0))
			entry.bind('<Down>', functools.partial(self.show_selfdefine_history, opt, 1))
		self.selfdefine_history_idx = {}
	
	def show_selfdefine_history(self, opt, dir, event):
		historylst = SELFDEFINE_HISTORY_DATA.get(str(opt), {}).get('batch', [])
		idx = self.selfdefine_history_idx.get(opt, 0)
		
		n = len(historylst)
		
		if dir == 0:  # 往上
			idx -= 1
		elif dir == 1:  # 往下
			idx += 1
		if -n <= idx < 0:
			self.selfdefine_history_idx[opt] = idx
			event.widget.delete(0, 'end')
			event.widget.insert(0, historylst[idx])
	
	def show_history(self, num):
		iplst = BATCH_HISTORY_DATA.get(str(num), [])
		if iplst:
			self.m_text.delete("1.0", "end")
			self.m_text.insert('1.0', '\n'.join(iplst))
	
	def save(self, num):
		iscorrect, iplist = self.IsTextCorrect('保存', False)
		if not iscorrect:
			return
		
		old = BATCH_HISTORY_DATA.get(str(num))
		if iplist:
			if old == iplist:
				return
			
			if old and not popup.double_confirm('保存', '你确定要覆盖编号%d中的内容吗？' % num):
				return
			
			SetBatchHistory(num, iplist)
			
			self.m_save_buttons[num][0]['fg'] = 'blue'
			self.m_save_buttons[num][1]['fg'] = 'blue'
		else:
			if old and not popup.double_confirm('保存', '你确定要清除编号%d中的内容吗？' % num):
				return
			
			SetBatchHistory(num, [])
			
			self.m_save_buttons[num][0]['fg'] = 'black'
			self.m_save_buttons[num][1]['fg'] = 'black'
	
	def IsTextCorrect(self, title, check_empty=True):
		width = (60, 300)
		text = self.m_text.get('1.0', 'end').strip()
		if check_empty and not text:
			popup.showerror(title, '请输入服务器IP', width)
			return False, []
		
		if text:
			iplist = [ip.strip() for ip in text.split('\n')]
			tmp = [ip for ip in iplist if ip not in serverlist.SERVER_DATA]
			if tmp:
				popup.showerror(title, '仅支持【服务器】面板中的服务器IP,以下IP无效：\n%s'% '\n'.join(tmp), width)
				return False, []
				
			tmp = [ip for ip in iplist if set(serverlist.SERVER_DATA[ip]['srv_type']).isdisjoint(set([SERVERTYPE_GAME, SERVERTYPE_KUAFU]))]
			if tmp:
				popup.showerror(title, '以下服既不是游戏服也不是跨服，属无效IP：\n%s' % '\n'.join(tmp), width)
				return False, []
		else:
			iplist = []
		
		return True, iplist
	
	def DoSelfdefineCommand(self, opt, event):
		from ui import mainframe
		iscorrect, iplist = self.IsTextCorrect('执行命令')
		if not iscorrect or not iplist:
			return
		
		if not popup.double_confirm('执行命令', '确定对以上服务器执行此命令吗？'):
			return
		
		msg = event.widget.get().strip()
		if msg:
			for ip in iplist:
				mainframe.g_MsgWin.AddPage(ip)
				mainframe.g_MsgWin.ChangePage(ip)
				windowoperate.g_OptManager.AddOpt(ip, opt, msg)
			historylst = SELFDEFINE_HISTORY_DATA.setdefault(str(opt), {}).setdefault('batch', [])
			historylst.append(msg)
			if len(historylst) > MAX_HISTORY_CNT:
				SELFDEFINE_HISTORY_DATA[str(opt)]['batch'] = historylst[len(historylst)-MAX_HISTORY_CNT: ]
			WriteJsonFile(SELFDEFINE_CMD_HISTORY_FILE, SELFDEFINE_HISTORY_DATA)
	
	def DoDate(self):
		from ui import mainframe
		iscorrect, iplist = self.IsTextCorrect('调时')
		if not iscorrect or not iplist:
			return
			
		default_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		timestr = simpledialog.askstring('调时', '请输入时间（年-月-日 时:分:秒）', initialvalue=default_time, parent=mainframe.g_App)
		if timestr:
			for ip in iplist:
				mainframe.g_MsgWin.AddPage(ip)
				mainframe.g_MsgWin.ChangePage(ip)
				windowoperate.g_OptManager.AddOpt(ip, OPT_DATE, timestr.strip())
	
	def DoUpdateCodeWithRevision(self, event):
		from ui import mainframe
		revision = simpledialog.askstring('code', '请输入版本号：', parent=mainframe.g_App)
		try:
			revision = int(revision.strip())
		except:
			popup.showerror('代码版本号 error', '请填入正确的整数')
			return
		self.DoUpdateCode(revision)
	
	def DoUpdateCode(self, revision=None):
		from ui import mainframe
		iscorrect, iplist = self.IsTextCorrect('更新代码')
		if not iscorrect or not iplist:
			return
	
		for ip in iplist:
			mainframe.g_MsgWin.AddPage(ip)
			mainframe.g_MsgWin.ChangePage(ip)
			opts = GetOptByType(ip, 1)
			for opt in opts:
				if revision is None:
					windowoperate.g_OptManager.AddOpt(ip, opt)
				else:
					windowoperate.g_OptManager.AddOpt(ip, opt, revision)
	
	def DoRebootProc(self):
		from ui import mainframe
		iscorrect, iplist = self.IsTextCorrect('重启')
		if not iscorrect or not iplist:
			return
		
		if not popup.double_confirm('重启', '你确定要重启这些服务器吗'):
			return
		
		for ip in iplist:
			mainframe.g_MsgWin.AddPage(ip)
			mainframe.g_MsgWin.ChangePage(ip)
			opts = GetOptByType(ip, 2)
			for opt in opts:
				windowoperate.g_OptManager.AddOpt(ip, opt)
	
	def DoTraceLog(self):
		from ui import mainframe
		iscorrect, iplist = self.IsTextCorrect('日志追踪')
		if not iscorrect or not iplist:
			return
		
		for ip in iplist:
			mainframe.g_MsgWin.AddPage(ip)
			mainframe.g_MsgWin.ChangePage(ip)
			opts = GetOptByType(ip, 3)
			for opt in opts:
				windowoperate.g_OptManager.AddOpt(ip, opt)
	
	def Show(self):
		self.selfdefine_history_idx = {}
	
	def Hide(self):
		pass

def SetBatchHistory(n, iplist):
	n = str(n)
	change = False
	if iplist:
		if iplist != BATCH_HISTORY_DATA.get(n):
			change = True
			BATCH_HISTORY_DATA[n] = iplist
	else:
		if n in BATCH_HISTORY_DATA:
			change = True
			BATCH_HISTORY_DATA.pop(n)
	
	if change:
		with open(BATCH_HISTORY_FILE, 'w') as f:
			json.dump(BATCH_HISTORY_DATA, f, indent=8, ensure_ascii=False)

def GetOptByType(ip, tp):
	opts = []
	if tp == 1:#更新
		if SERVERTYPE_GAME in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_UPDATECODE]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_UPDATE_PISCES]
				else:
					opts = [OPT_UPDATE_JZ]
		elif SERVERTYPE_KUAFU in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_UPDATE_CENTER, OPT_UPDATE_BATTLE, ]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_UPDATE_CENTER_PISCES, OPT_UPDATE_BATTLE_PISCES]
				else:
					opts = [OPT_UPDATE_CENTER_JZ, OPT_UPDATE_BATTLE_JZ]
	elif tp == 2:#重启
		if SERVERTYPE_GAME in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_REBOOTGAME]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_REBOOT_PISCES]
				else:
					opts = [OPT_REBOOT_JZ]
		elif SERVERTYPE_KUAFU in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_REBOOT_BATTLE, OPT_REBOOT_CENTER, ]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_REBOOT_BATTLE_PISCES, OPT_REBOOT_CENTER_PISCES]
				else:
					opts = [OPT_REBOOT_BATTLE_JZ, OPT_REBOOT_CENTER_JZ]
	elif tp == 3:#看日志
		if SERVERTYPE_GAME in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_TRACELOG]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_TRACELOG_PISCES]
				else:
					opts = [OPT_TRACELOG_JZ]
		elif SERVERTYPE_KUAFU in serverlist.SERVER_DATA[ip]['srv_type']:
			opts = [OPT_TRACELOG_BATTLE, OPT_TRACELOG_CENTER, ]
			if serverlist.SERVER_DATA[ip]['user_type'] is USERTYPE_DEVELOPER:
				if BATCH_CONFIG_DATA.get(ip, BATCH_SET_DATA[0]) == '桃手生效':
					opts = [OPT_TRACELOG_BATTLE_PISCES, OPT_TRACELOG_CENTER_PISCES]
				else:
					opts = [OPT_TRACELOG_BATTLE_JZ, OPT_TRACELOG_CENTER_JZ]
	return opts
