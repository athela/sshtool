# -*- coding: gbk -*-

from tkinter import *
from tkinter import ttk
from tkinter import scrolledtext
from ui import serverframe
from ui import batchframe
from define import *
import functools
import os
import windowoperate
from game import serverlist

#客户端服务器列表： https://docs.qq.com/sheet/DU1FQVG51aFppenhz
HELP = '''
使用说明：
	1. 进入服务器页面，默认刷新基本信息
		手动点刷新，刷新进程信息，开发服会输出当前代码版本信息
	2. 更新代码到某个版本号，在更新按钮上使用右键；认证、datasrv、地图的更新也支持这样使用
	3. 调时，输入框默认显示该服当前时间
	4. 开发服的更新/重启/看日志/配置，区分了九州和桃手
	5. 策划服提供，可导所有表格、可导单个表格
		选[查询]点击导表，下拉框更新最新的表格列表
		导单个或所有表格，选表格选项 或者 填入 skill_srv 类似标签
		导多个表，手动输入如：skill_srv,buff_srv,fuli_srv
	6. 日志 输出已有的历史日志，追踪日志 持续输出实时日志(如有)，同时button变色，再次点击会停止输出
		追踪日志时，不影响其它按钮的输出
	7. 跨服或开发服同时开两个日志追踪时，分栏显示, 停止该追踪，该栏消失
		适合跨服同时显示主控和战斗服的日志
	8. 更改服务器配置game.ini
		展示了常用配置的修改
		未展示的配置，可通用[自定义]区域修改或添加
	9. TelentDebug功能，连接服务器debug端口交互
		支持上下键翻看历史输入过的指令
	10. [服务器]和[批量]预留了linux系统命令和sudo指令，可自由输入
		支持上下键翻看历史输入过的指令
	11. [批量]可对多个服务器同时调时，更新，重启，看日志
		批量更新，右键，可输入版本号
	12. 日志 可查看其它日志文件，在日志按钮上右键输入不带.log后缀的文件名，如 gm
	13. 单击或双击 右边输出框的 服务器名button, 左边的操作框 会跳到该 服务器的操作页面
	14. 可根据需要修改exe目录下的config.json文件
		user_department: 用户类型
		append_server_list: 支持本地增加[使用通用指令]的游戏服列表
		增加[使用非通用指令]的服务器请开发人员添加并重新打包
'''

WINDOW_HEIGHT = 600
WINDOW_WIDTH_MAIN = 480
WINDOW_WIDTH_MESSAGE = 550

class Application(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)

		ttk.Separator(self, orient='horizontal').pack(fill="x")	#分隔条
		self.head = Frame(self, height=40)
		self.head.pack_propagate(0)
		self.head.pack(side="top", expand="no", fill="both")

		ttk.Separator(self, orient='horizontal').pack(fill="x")
		self.tabs = {}  # 最左边的button列表，'服务器'是第一个
		self.cur_tab_name = None
		self.cur_tab_var = StringVar()
		self.tabframe = Frame(self, width=60)
		self.tabframe.pack_propagate(0)
		self.tabframe.pack(side="left", expand="no", fill="both")

		ttk.Separator(self, orient='vertical').pack(side="left", fill="y")
		self.pages = {}	#tab对应的响应页面
		self.content = Frame(self)
		self.content.pack_propagate(0)
		self.content.pack(expand="yes", fill="both")
		self.CreatePages()
	
	def SwitchPage(self):
		name = self.cur_tab_var.get()
		
		if name != self.cur_tab_name:
			if self.cur_tab_name:
				self.pages[self.cur_tab_name].pack_forget()
				self.pages[self.cur_tab_name].Hide()
			self.cur_tab_name = name
			self.pages[name].Show()
			self.pages[name].pack(expand="yes", fill="both")
	
	def CreatePages(self):
		self.DoCreatePage('服务器', serverframe)
		self.DoCreatePage('批量', batchframe)
		self.cur_tab_var.set('服务器')
		self.SwitchPage()
	
	def DoCreatePage(self, name, module):
		f = Frame(self.tabframe, height=40)
		f.pack_propagate(0)
		f.pack(fill="x")
		bt = Radiobutton(f, bd=3, bg='lightgrey', indicatoron=0, command=self.SwitchPage, font=("微软雅黑", 12, "normal"), variable=self.cur_tab_var, text=name, value=name)
		bt.pack(expand="yes", fill="both")
		
		page = module.PageFrame(self.content)
		page.pack_propagate(0)
		self.tabs[name] = bt
		self.pages[name] = page

class MessageWindow(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)
		f = Frame(self)
		f.pack(expand='yes', fill='both')
		self.titlebar = Frame(f)
		self.titlebar.pack(fill='x')
		self.titlebar_serverlst = []
		self.textblock = Frame(f)
		self.textblock.pack(expand='yes', fill='both')
		self.text_pages = {}
		self.telnet_history_index = {}
		self.AddPage(DEFAULT_CONSOLE_ID)
		self.ChangePage(DEFAULT_CONSOLE_ID)
	
	def AddPage(self, ip, opt=OPT_SSH_WINDOW):
		if opt is not OPT_SSH_WINDOW:
			self.telnet_history_index[ip] = 0
			self.RefreshDebugState(ip, opt)
		key = (ip, opt)
		if key in self.text_pages:
			return
		
		name = "说明" if ip == DEFAULT_CONSOLE_ID else serverlist.GetServerName(ip) if opt is OPT_SSH_WINDOW else serverlist.GetServerName(ip)+OPT_NAME[opt]
		bt1 = Radiobutton(self.titlebar, indicatoron=0, command=functools.partial(self._OnChangePage, ip, opt), font=('黑体', 10, 'normal'), value=(ip, opt), text=name, bd=2)
		if ip != DEFAULT_CONSOLE_ID:
			bt1.bind('<Double-Button-1>', functools.partial(self.ShowServerPage, ip))
			bt1.bind('<Button-1>', functools.partial(self.ShowServerPage, ip))
		bt1.pack(side='left', padx=0)
		
		f1 = Frame(self.titlebar, width=20, height=22)
		f1.pack_propagate(False)
		f1.pack(side='left')
		bt2 = Button(f1, text='x', bd=1, command=functools.partial(self.ClosePage, ip, opt))
		if ip == DEFAULT_CONSOLE_ID:
			f1['width'] = 7
		else:
			bt2.place(x=0, y=-4)
		
		txt = scrolledtext.ScrolledText(self.textblock, state='disabled', bd=3, )
		txt.pack(expand='yes', fill='both')
		if ip == DEFAULT_CONSOLE_ID:
			txt['state'] = 'normal'
			txt.insert('end', HELP)
			txt['state'] = 'disabled'
		
		if opt is OPT_SSH_WINDOW:
			self.text_pages[key] = [bt1, bt2, f1, txt]
		else:
			txt2 = Text(self.textblock, bd=3)
			txt2.pack(expand='yes', fill='both')
			
			def do_something1(event):
				pass

			txt2.bind('<Shift-Return>', do_something1)
			txt2.bind('<Control-Return>', do_something1)
			txt2.bind('<Return>', functools.partial(self.TelnetEnter, ip, opt))
			txt2.bind('<Up>', functools.partial(self.TelnetHistory, ip, 0))
			txt2.bind('<Down>', functools.partial(self.TelnetHistory, ip, 1))
			
			self.text_pages[key] = [bt1, bt2, f1, txt, txt2]
		
		self.titlebar_serverlst.append(key)
		self.ChangePage(ip, opt)
	
	def TelnetHistory(self, ip, dir, event):
		def show_history_msg(ip, idx, msg):
			self.telnet_history_index[ip] = idx
			event.widget.delete('1.0', end)
			event.widget.insert('end', msg)
			# event.widget.mark_set("insert", "%d.%d" % (row + 1, col + 1))
			event.widget.see('end')
		
		cur_row = int(float(event.widget.index("insert")))
		end = event.widget.index("end")
		end_row = int(float(end))
		
		idx = self.telnet_history_index.get(ip, 0)
		lst = TELNET_HISTORY_DATA.get(ip, [])
		n = len(lst)
		if cur_row == 1 and dir == 0:	#往上，行从1开始，列从0开始
			idx -= 1
			if -n <= idx < 0:
				show_history_msg(ip, idx, lst[idx])
		elif cur_row == end_row - 1 and dir == 1: #往下
			idx += 1
			if -n <= idx < 0:
				show_history_msg(ip, idx, lst[idx])
	
	def TelnetEnter(self, ip, opt, event):
		msg = event.widget.get('0.0', 'end')
		event.widget.delete('0.0', 'end')
		self.AppendConsoleMessage(ip, msg, False, opt)
		msg = msg.strip()
		if msg:
			lst = TELNET_HISTORY_DATA.setdefault(ip, [])
			lst.append(msg)
			if len(lst) > MAX_HISTORY_CNT:
				TELNET_HISTORY_DATA[ip] = lst[len(lst)-MAX_HISTORY_CNT: ]
			self.telnet_history_index[ip] = 0
			windowoperate.g_OptManager.AddOpt(ip, OPT_DEBUG_WRITE, opt, msg)
		return 'break'
	
	def ChangePage(self, ip, opt=OPT_SSH_WINDOW):
		lst = self.text_pages.get((ip, opt))
		if lst:
			lst[0].invoke()
	
	def _OnChangePage(self, ip, opt):
		for key, controls in self.text_pages.items():
			if key == (ip, opt):
				for textctrl in controls:
					if isinstance(textctrl, (scrolledtext.ScrolledText, Text, Entry)):
						textctrl.pack(expand='yes', fill='both')
			else:
				for textctrl in controls:
					if isinstance(textctrl, (scrolledtext.ScrolledText, Text, Entry)):
						textctrl.pack_forget()
	
	def ShowServerPage(self, ip, event):
		if g_App.cur_tab_name != '服务器':
			g_App.tabs['服务器'].invoke()
		g_App.pages['服务器'].SelectServer(ip)
	
	def ClosePage(self, ip, opt):
		key = (ip, opt)
		if ip == DEFAULT_CONSOLE_ID or key not in self.text_pages:
			return
		
		if opt is not OPT_SSH_WINDOW:
			self.telnet_history_index.pop(ip, None)
		
		ctrls = self.text_pages.pop(key, None)
		idx = self.titlebar_serverlst.index(key)
		self.titlebar_serverlst.pop(idx)
		
		for textctrl in ctrls:	#这段不能去掉
			if isinstance(textctrl, scrolledtext.ScrolledText):
				textctrl.pack_forget()
		for textctrl in ctrls:
			textctrl.destroy()
		
		if len(self.titlebar_serverlst) > 0:
			newidx = idx if idx < len(self.titlebar_serverlst) else idx-1
			newkey = self.titlebar_serverlst[newidx]
			self.text_pages[newkey][0].invoke()
		
		windowoperate.g_OptManager.AddOpt(ip, OPT_CLOSE_PAGE, opt)
	
	def AddSecondScrolledText(self, ip):
		key = (ip, OPT_SSH_WINDOW)
		if key not in self.text_pages:
			return
		
		if len(self.text_pages[key]) == 4:
			textcontrol = scrolledtext.ScrolledText(self.textblock, state='disabled', bd=3, )
			textcontrol.pack(expand='yes', fill='both')
			self.text_pages[key].append(textcontrol)
	
	def RemoveSecondScrolledText(self, ip):
		key = (ip, OPT_SSH_WINDOW)
		if key not in self.text_pages:
			return
		
		if len(self.text_pages[key]) == 5:
			textcontrol = self.text_pages[key].pop(4)
			textcontrol.pack_forget()
			textcontrol.destroy()
	
	def AppendConsoleMessage(self, ip, msg, second_scrolltext=False, win_opt=OPT_SSH_WINDOW):
		key = (ip, win_opt)
		if key not in self.text_pages:
			return
		
		if second_scrolltext:
			if len(self.text_pages[key]) == 5:
				textcontrol = self.text_pages[key][4]
			else:
				textcontrol = None
		else:
			textcontrol = self.text_pages[key][3]
		if textcontrol:
			textcontrol['state'] = 'normal'
			textcontrol.insert('end', msg)
			end_line_number = int(float(textcontrol.index('end')))
			if end_line_number > MAX_MESSAGE_LINE:
				textcontrol.delete('1.0', '%d.0' % ((end_line_number - MAX_MESSAGE_LINE) + 1))
			textcontrol.see('end')
			textcontrol['state'] = 'disabled'
	
	def RefreshDebugState(self, ip, opt, disconnect=None):
		v = self.text_pages.get((ip, opt))
		if v:
			if disconnect:
				v[1]['bg'] = 'red'
			else:
				v[1]['bg'] = 'SystemButtonFace'

def WindowInit(tk):
	global g_MsgWin, g_App
	app = Application(master=tk, width=WINDOW_WIDTH_MAIN, height=WINDOW_HEIGHT)
	app.pack_propagate(0)	#父组件不会自动调节尺寸以容纳所有子组件，父组件窗口的高度和宽度设置才可以生效
	app.pack(side='left', fill='y')
	g_App = app
	ttk.Separator(tk, orient='vertical').pack(side="left", fill="y")
	
	msg = MessageWindow(tk, width=WINDOW_WIDTH_MESSAGE, height=WINDOW_HEIGHT)
	msg.pack_propagate(0)
	msg.pack(side='left', expand='yes', fill='both')
	g_MsgWin = msg
	
	tk_start_x = (tk.winfo_screenwidth() - (WINDOW_WIDTH_MAIN + WINDOW_WIDTH_MESSAGE)) / 2
	tk_start_y = (tk.winfo_screenheight() - WINDOW_HEIGHT) / 2
	tk.geometry('%dx%d+%d+%d' % (WINDOW_WIDTH_MAIN + WINDOW_WIDTH_MESSAGE, WINDOW_HEIGHT, tk_start_x, tk_start_y))
	
	if os.path.exists('image.ico'):
		tk.iconbitmap('image.ico')
	tk.minsize(WINDOW_WIDTH_MAIN, WINDOW_HEIGHT)
	tk.title("内服工具%s.%s.%s" % tuple(APP_VERSION))

if 'g_MsgWin' not in globals().keys():
	g_App = None
	g_MsgWin = None
