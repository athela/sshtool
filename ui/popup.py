# -*- coding: gbk -*-

from tkinter import *
from tkinter import scrolledtext


DEFAULT_SIZE = (300, 100)
DEFAULT_POS = (100, 200)
DEFAULT_LABEL_SIZE = (36, 270)

class Popup(Toplevel):
	def __init__(self, title=None):
		from ui import mainframe
		
		parent = mainframe.g_App
		Toplevel.__init__(self, parent)
		
		self.withdraw()  # remain invisible for now
		# If the master is not viewable, don't
		# make the child transient, or else it
		# would be opened withdrawn
		if parent.winfo_viewable():
			self.transient(parent)
		
		if title:
			self.title(title)
		
		self.parent = parent
		
		self.initial_focus = self
		
		self.result = False
		self._isdestroyed = False
		self._win_size = None
		self._win_pos = None
		
		self.allow_close = True
		self.protocol("WM_DELETE_WINDOW", self.cancel)
	
	def setfocus(self, widget):
		self.initial_focus = widget
	
	def setsize(self, size):
		self._win_size = size
	
	def setpos(self, pos):
		self._win_pos = pos
	
	def display(self):  # 阻塞
		if self.parent is not None:
			relx, rely = 0, 0
			if self._win_pos:
				relx, rely = self._win_pos
			x, y = self.parent.winfo_rootx() + relx, self.parent.winfo_rooty() + rely
			if self._win_size:
				self.geometry("%dx%d+%d+%d" % (self._win_size[0], self._win_size[1], x, y))
			else:
				self.geometry("+%d+%d" % (x, y))
		
		self.deiconify()  # become visibile now
		
		self.initial_focus.focus_set()
		
		# wait for window to appear on screen before calling grab_set
		self.wait_visibility()
		self.grab_set()
		self.wait_window(self)
	
	def forbid_close(self):
		self.allow_close = False
	
	def permit_close(self):
		self.allow_close = True
	
	def destroy(self):
		'''Destroy the window'''
		self._isdestroyed = True
		self.initial_focus = None
		Toplevel.destroy(self)
	
	def isdestroyed(self):
		return self._isdestroyed
	
	def ok(self, event=None):
		if self.allow_close:
			self.result = True
			self.withdraw()
			self.update_idletasks()
			self.cancel()
	
	def cancel(self, event=None):
		if self.allow_close:
			# put focus back to the parent window
			if self.parent is not None:
				self.parent.focus_set()
			self.destroy()
	
	def button_ok(self):
		box = Frame(self)
		w = Button(box, text="确定", width=10, command=self.ok, default=ACTIVE)
		w.pack(side=LEFT, padx=5, pady=5)
		# self.bind("<Return>", self.ok)
		box.pack()
	
	def button_ok_cancel(self):
		box = Frame(self)
		w = Button(box, text="确定", width=10, command=self.ok, default=ACTIVE)
		w.pack(side=LEFT, padx=5, pady=5)
		w = Button(box, text="取消", width=10, command=self.cancel)
		w.pack(side=LEFT, padx=5, pady=5)
		# self.bind("<Return>", self.ok)
		# self.bind("<Escape>", self.cancel)
		box.pack()

class _LablePopup(Popup):
	def __init__(self, title=None, text=None, width=None):
		Popup.__init__(self, title)
		
		self.label = Label(self, text=text, font=('', 10))
		if width:
			self.label['width'] = width[0]
			self.label['wraplength'] = width[1]
		self.label.pack(expand='yes', padx=15, pady=10)

def double_confirm(title, text, width=DEFAULT_LABEL_SIZE, pos=DEFAULT_POS):
	p = _LablePopup(title, text, width)
	p.setpos(pos)
	p.button_ok_cancel()
	p.display()
	return p.result

def showerror(title, text, width=DEFAULT_LABEL_SIZE, pos=DEFAULT_POS):
	p = _LablePopup(title, text, width)
	p.setpos(pos)
	
	box = Frame(p)
	w = Button(box, text="确定", width=10, command=p.cancel, default=ACTIVE)
	w.pack(side=LEFT, padx=5, pady=5)
	box.pack()
	p.display()

def scroll_text(texts, title=None):
	window = Popup(title)
	h = min(max(len(texts)+2, 10),  30)
	textcontrol = scrolledtext.ScrolledText(window, width=50, height=h, bd=3, font=('', 12), state='disabled')
	textcontrol['state'] = 'normal'
	textcontrol.insert('end', '\n'.join(texts))
	textcontrol['state'] = 'disabled'
	textcontrol.pack(expand='yes', fill='both')
	window.setfocus(textcontrol)
	window.setpos((60, 100))
	window.display()


