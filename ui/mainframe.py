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

#�ͻ��˷������б� https://docs.qq.com/sheet/DU1FQVG51aFppenhz
HELP = '''
ʹ��˵����
	1. ���������ҳ�棬Ĭ��ˢ�»�����Ϣ
		�ֶ���ˢ�£�ˢ�½�����Ϣ���������������ǰ����汾��Ϣ
	2. ���´��뵽ĳ���汾�ţ��ڸ��°�ť��ʹ���Ҽ�����֤��datasrv����ͼ�ĸ���Ҳ֧������ʹ��
	3. ��ʱ�������Ĭ����ʾ�÷���ǰʱ��
	4. �������ĸ���/����/����־/���ã������˾��ݺ�����
	5. �߻����ṩ���ɵ����б�񡢿ɵ��������
		ѡ[��ѯ]�������������������µı���б�
		�����������б��ѡ���ѡ�� ���� ���� skill_srv ���Ʊ�ǩ
		��������ֶ������磺skill_srv,buff_srv,fuli_srv
	6. ��־ ������е���ʷ��־��׷����־ �������ʵʱ��־(����)��ͬʱbutton��ɫ���ٴε����ֹͣ���
		׷����־ʱ����Ӱ��������ť�����
	7. ����򿪷���ͬʱ��������־׷��ʱ��������ʾ, ֹͣ��׷�٣�������ʧ
		�ʺϿ��ͬʱ��ʾ���غ�ս��������־
	8. ���ķ���������game.ini
		չʾ�˳������õ��޸�
		δչʾ�����ã���ͨ��[�Զ���]�����޸Ļ����
	9. TelentDebug���ܣ����ӷ�����debug�˿ڽ���
		֧�����¼�������ʷ�������ָ��
	10. [������]��[����]Ԥ����linuxϵͳ�����sudoָ�����������
		֧�����¼�������ʷ�������ָ��
	11. [����]�ɶԶ��������ͬʱ��ʱ�����£�����������־
		�������£��Ҽ���������汾��
	12. ��־ �ɲ鿴������־�ļ�������־��ť���Ҽ����벻��.log��׺���ļ������� gm
	13. ������˫�� �ұ������� ��������button, ��ߵĲ����� �������� �������Ĳ���ҳ��
	14. �ɸ�����Ҫ�޸�exeĿ¼�µ�config.json�ļ�
		user_department: �û�����
		append_server_list: ֧�ֱ�������[ʹ��ͨ��ָ��]����Ϸ���б�
		����[ʹ�÷�ͨ��ָ��]�ķ������뿪����Ա��Ӳ����´��
'''

WINDOW_HEIGHT = 600
WINDOW_WIDTH_MAIN = 480
WINDOW_WIDTH_MESSAGE = 550

class Application(Frame):
	def __init__(self, *args, **kwargs):
		Frame.__init__(self, *args, **kwargs)

		ttk.Separator(self, orient='horizontal').pack(fill="x")	#�ָ���
		self.head = Frame(self, height=40)
		self.head.pack_propagate(0)
		self.head.pack(side="top", expand="no", fill="both")

		ttk.Separator(self, orient='horizontal').pack(fill="x")
		self.tabs = {}  # ����ߵ�button�б�'������'�ǵ�һ��
		self.cur_tab_name = None
		self.cur_tab_var = StringVar()
		self.tabframe = Frame(self, width=60)
		self.tabframe.pack_propagate(0)
		self.tabframe.pack(side="left", expand="no", fill="both")

		ttk.Separator(self, orient='vertical').pack(side="left", fill="y")
		self.pages = {}	#tab��Ӧ����Ӧҳ��
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
		self.DoCreatePage('������', serverframe)
		self.DoCreatePage('����', batchframe)
		self.cur_tab_var.set('������')
		self.SwitchPage()
	
	def DoCreatePage(self, name, module):
		f = Frame(self.tabframe, height=40)
		f.pack_propagate(0)
		f.pack(fill="x")
		bt = Radiobutton(f, bd=3, bg='lightgrey', indicatoron=0, command=self.SwitchPage, font=("΢���ź�", 12, "normal"), variable=self.cur_tab_var, text=name, value=name)
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
		
		name = "˵��" if ip == DEFAULT_CONSOLE_ID else serverlist.GetServerName(ip) if opt is OPT_SSH_WINDOW else serverlist.GetServerName(ip)+OPT_NAME[opt]
		bt1 = Radiobutton(self.titlebar, indicatoron=0, command=functools.partial(self._OnChangePage, ip, opt), font=('����', 10, 'normal'), value=(ip, opt), text=name, bd=2)
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
		if cur_row == 1 and dir == 0:	#���ϣ��д�1��ʼ���д�0��ʼ
			idx -= 1
			if -n <= idx < 0:
				show_history_msg(ip, idx, lst[idx])
		elif cur_row == end_row - 1 and dir == 1: #����
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
		if g_App.cur_tab_name != '������':
			g_App.tabs['������'].invoke()
		g_App.pages['������'].SelectServer(ip)
	
	def ClosePage(self, ip, opt):
		key = (ip, opt)
		if ip == DEFAULT_CONSOLE_ID or key not in self.text_pages:
			return
		
		if opt is not OPT_SSH_WINDOW:
			self.telnet_history_index.pop(ip, None)
		
		ctrls = self.text_pages.pop(key, None)
		idx = self.titlebar_serverlst.index(key)
		self.titlebar_serverlst.pop(idx)
		
		for textctrl in ctrls:	#��β���ȥ��
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
	app.pack_propagate(0)	#����������Զ����ڳߴ��������������������������ڵĸ߶ȺͿ�����òſ�����Ч
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
	tk.title("�ڷ�����%s.%s.%s" % tuple(APP_VERSION))

if 'g_MsgWin' not in globals().keys():
	g_App = None
	g_MsgWin = None
