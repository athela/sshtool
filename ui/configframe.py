# -*- coding: gbk -*-

from tkinter import *
from tkinter import ttk
from define import *
from ui import popup
from game.gameconfig import *
from game import serverlist
from game.command import *
import time
import windowoperate
import functools

GAME_CONFIG = [OPT_GAMECONFIG, OPT_GAMECONFIG_PISCES, OPT_GAMECONFIG_JZ]
BATTLE_CONFIG = [OPT_GAMECONFIG_BATTLE, OPT_GAMECONFIG_BATTLE_JZ, OPT_GAMECONFIG_BATTLE_PISCES]
CENTER_CONFIG = [OPT_GAMECONFIG_CENTER, OPT_GAMECONFIG_CENTER_JZ, OPT_GAMECONFIG_CENTER_PISCES]
FORBIT_EDIT = ['srvid', 'srvname', ]

POPUP_HEIGHT = 220
CONFIG_HEIGHT = 180

class ConfigFrame(Frame):
	def __init__(self, parent, cfgdata, ip, opt, *args, **kwargs):
		Frame.__init__(self, parent, *args, **kwargs)
		self.cfgdata = cfgdata
		self.ip = ip
		self.opt = opt
		self.controls = {}
		self.comb_keys = []
		self.entry_keys = []
		
		def _create_line(parent, name):
			f = Frame(parent)
			f.pack(fill='x')
			Label(f, text=name, font=('微软雅黑', 10)).pack(side='left')
			return f
		
		def _entry(parent, name, **kkargs):
			e = Entry(parent, state='readonly', font=('微软雅黑', 10), justify='center', fg='black', **kkargs)
			e.pack(side='left', padx=3, pady=3)
			self.controls[name] = e
			self.entry_keys.append(name)
		
		def _combo(parent, name, value=('开启', '关闭'), **kkargs):
			c = ttk.Combobox(parent, value=value, state='disabled', justify='center',  **kkargs)
			c.pack(side='left', padx=3, pady=3)
			self.controls[name] = c
			self.comb_keys.append(name)
			
		#具体配置区
		f2 = Frame(self)
		f2.pack(fill='x')
		
		left = Frame(f2, width=190, height=CONFIG_HEIGHT)
		left.pack_propagate(0)
		left.pack(side='left')

		right = Frame(f2, width=190, height=CONFIG_HEIGHT)
		right.pack_propagate(0)
		right.pack(side='right')

		f = _create_line(left, '服务器ID')
		_entry(f, 'srvid')
		f = _create_line(left, '开服时间')
		_entry(f, 'open_time')
		f = _create_line(left, '测试模式')
		_combo(f, 'testsrv')
		if opt in GAME_CONFIG:
			f = _create_line(left, '主控ip')
			_entry(f, 'proxyhost')
			f = _create_line(left, '竞技场主控ip')
			_entry(f, 'grouphost')
		elif opt in BATTLE_CONFIG:
			f = _create_line(left, '主控ip')
			_entry(f, 'proxyhost')
			f = _create_line(left, '战斗服类型')
			_combo(f, 'combatserver', list(COMBATSERVER_TYPE_NAME.keys()))
			f = _create_line(left, '竞技场主控ip')
			_entry(f, 'centerhost')
		elif opt in CENTER_CONFIG:
			f = _create_line(left, '主控标识')
			_combo(f, 'proxyserver')
			f = _create_line(left, '竞技场主控标识')
			_combo(f, 'centersrv')
			f = _create_line(left, '竞技场主控端口')
			_entry(f, 'groupport')
			
		f = _create_line(right, '服务器名称')
		_entry(f, 'srvname')
		f = _create_line(right, 'debug端口')
		_entry(f, 'debug')
		f = _create_line(right, '机器人')
		_combo(f, 'closerobot')
		if opt in GAME_CONFIG:
			f = _create_line(right, '主控端口')
			_entry(f, 'proxyport')
			f = _create_line(right, '竞技场主控端口')
			_entry(f, 'groupport')
		elif opt in BATTLE_CONFIG:
			f = _create_line(right, '主控端口')
			_entry(f, 'proxyport')
			f = _create_line(right, '竞技场战斗服标识')
			_combo(f, 'groupsrv')
			f = _create_line(right, '竞技场主控端口')
			_entry(f, 'centerport')
		elif opt in CENTER_CONFIG:
			f = _create_line(right, '主控端口')
			_entry(f, 'proxyport')
			f = _create_line(right, '竞技场主控标识2')
			_combo(f, 'groupsrv')
			
		# 自定义配置区
		f1 = Frame(self)
		f1.pack(fill='x')
		Label(f1, text='自定义').pack(side='left')
		sections = self.cfgdata.GetSections()
		_combo(f1, 'selfdefine_section', sections, width=10)
		_entry(f1, 'selfdefine_key', width=12)
		_entry(f1, 'selfdefine_value', width=18)
		self.SetData()
	
	def EditEnable(self):
		for name, control in self.controls.items():
			if name in FORBIT_EDIT:
				continue
			if isinstance(control, ttk.Combobox):
				control['state'] = 'readonly'
			else:
				control['state'] = 'normal'
	
	def EditDisable(self):
		for name, control in self.controls.items():
			if isinstance(control, ttk.Combobox):
				control['state'] = 'disabled'
			else:
				control['state'] = 'readonly'
	
	def Restore(self):
		self.SetData()
	
	def SetData(self):
		for name in self.entry_keys:
			value = self.cfgdata.Get(name)
			if value is None:
				continue
			try:
				if name == 'open_time':
					value = time.strftime('%Y-%m-%d %H:%M', time.localtime(int(value)))
			except:
				pass
			control = self.controls[name]
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, value)
			control['state'] = 'readonly'
			
		for name in self.comb_keys:
			value = self.cfgdata.Get(name)
			if value is None:
				continue
			try:
				if name in ['testsrv', 'groupsrv', 'centersrv', 'proxyserver']:
					value = '关闭' if not int(value) else '开启'
				elif name == 'closerobot':
					value = '开启' if not int(value) else '关闭'
				elif name == 'combatserver':
					value = COMBATSERVER_TYPE_KEY.get(int(value), value)
			except:
				pass
			else:
				control = self.controls[name]
				control.set(value)
		
	def SetArenaKuafu(self):
		if self.opt in CENTER_CONFIG:
			#设置上：
			self.controls['groupsrv'].set("开启")
			self.controls['centersrv'].set("开启")
			control = self.controls['groupport']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.cfgdata.Get('groupport'))
			control['state'] = 'readonly'
			
			#取消掉：
			self.controls['proxyserver'].set("关闭")
		elif self.opt in BATTLE_CONFIG:
			#设置上
			self.controls['groupsrv'].set("开启")
			
			control = self.controls['centerhost']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.ip)
			control['state'] = 'readonly'
			
			control = self.controls['centerport']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.cfgdata.Get('centerport'))
			control['state'] = 'readonly'
			
			#取消掉
			control = self.controls['proxyhost']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, GAMECONFIG_DEFAULT_VALUE['proxyhost'])
			control['state'] = 'readonly'
			
			self.controls['combatserver'].set(COMBATSERVER_TYPE_KEY[0])
	
	def SetNormalKuafu(self):
		if self.opt in CENTER_CONFIG:
			# 取消掉：
			self.controls['groupsrv'].set("关闭")
			self.controls['centersrv'].set("关闭")
			
			# 设置上：
			self.controls['proxyserver'].set("开启")
			control =self.controls['proxyport']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.cfgdata.Get('proxyport'))
			control['state'] = 'readonly'
		elif self.opt in BATTLE_CONFIG:
			# 取消掉
			self.controls['groupsrv'].set("关闭")
			
			control = self.controls['centerhost']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, GAMECONFIG_DEFAULT_VALUE['centerhost'])
			control['state'] = 'readonly'
			
			# 设置上
			control = self.controls['proxyhost']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.ip)
			control['state'] = 'readonly'
			
			control = self.controls['proxyport']
			control['state'] = 'normal'
			control.delete(0, 'end')
			control.insert(0, self.cfgdata.Get('proxyport'))
			control['state'] = 'readonly'
			
			self.controls['combatserver'].set(COMBATSERVER_TYPE_KEY[3])
	
	def TryGetUIData(self):
		dct = {}
		new = None
		combkeys = self.comb_keys[:]
		entrykeys = self.entry_keys[:]
		
		cur_key = 'open_time'
		entrykeys.remove(cur_key)
		try:
			tmst = time.strptime(self.controls[cur_key].get(), '%Y-%m-%d %H:%M')
			dct[cur_key] = int(time.mktime(tmst))
		except:
			return False, '开服时间格式错误, 正确格式为: 2020-01-15 12:00'
			
		for cur_key in ['testsrv', 'groupsrv', 'centersrv', 'proxyserver']:
			if cur_key in combkeys:
				combkeys.remove(cur_key)
				control = self.controls[cur_key]
				dct[cur_key] = 1 if control.get() == '开启' else 0
		for cur_key in ['closerobot']:
			if cur_key in combkeys:
				combkeys.remove(cur_key)
				control = self.controls[cur_key]
				dct[cur_key] = 0 if control.get() == '开启' else 1
		
		cur_key = 'combatserver'
		if cur_key in combkeys:
			combkeys.remove(cur_key)
			combattype = self.controls[cur_key].get()
			dct[cur_key] = COMBATSERVER_TYPE_NAME.get(combattype, combattype)
		
		combkeys.remove('selfdefine_section')
		entrykeys.remove('selfdefine_key')
		entrykeys.remove('selfdefine_value')
		section, key, value = [self.controls[name].get().strip() for name in ['selfdefine_section', 'selfdefine_key', 'selfdefine_value']]
		if all([section, key, value]):
			if section == 'game':
				dct[key] = value
			else:
				new = [section, key, value]
		
		for cur_key in combkeys + entrykeys:
			dct[cur_key] = self.controls[cur_key].get()
		
		return True, (dct, new)

class ConfigPopup(popup.Popup):
	def __init__(self, ip, opt, cfgdata, *args, **kwargs):
		title = OPT_NAME[opt] if opt in OPT_NAME else '更改%s的配置'%serverlist.GetServerName(ip)
		popup.Popup.__init__(self, title, *args, **kwargs)
		self.ip = ip
		self.opt = opt
		
		self.config_frame = ConfigFrame(self, cfgdata, ip, opt, width=400, height=POPUP_HEIGHT)
		self.config_frame.pack_propagate(0)
		self.config_frame.pack(fill='x')
		
		self.cfgchange_frame = Frame(self)
		self.cfgchange_frame.pack()
		Button(self.cfgchange_frame, text="修改", width=10, command=self._edit_start).pack(side='left', padx=5, pady=5)
		user_type = serverlist.SERVER_DATA[ip]["user_type"]
		if user_type is USERTYPE_DEVELOPER and opt in BATTLE_CONFIG + CENTER_CONFIG:
			if opt in BATTLE_CONFIG:
				name1, name2 = '切到日常战斗服', '切到竞技场战斗服'
			elif opt in CENTER_CONFIG:
				name1, name2 = '切到日常主控', '切到竞技场主控'
			Button(self.cfgchange_frame, text=name1, command=self._switch_to_normal_kuafu).pack(side='left', padx=5, pady=5)
			Button(self.cfgchange_frame, text=name2, command=self._switch_to_arena_kuafu).pack(side='left', padx=5, pady=5)
		
		self.cfgconfirm_frame = Frame(self)	#初始未pack
		Button(self.cfgconfirm_frame, text="确定", width=10, command=self._edit_commit).pack(side='left', padx=5, pady=5)
		Button(self.cfgconfirm_frame, text="取消", width=10, command=self._edit_cancel).pack(side='left', padx=5, pady=5)
		
	def _switch_to_normal_kuafu(self):
		self.config_frame.SetNormalKuafu()
		self.cfgchange_frame.pack_forget()
		self.cfgconfirm_frame.pack()
	
	def _switch_to_arena_kuafu(self):
		self.config_frame.SetArenaKuafu()
		self.cfgchange_frame.pack_forget()
		self.cfgconfirm_frame.pack()
	
	def _edit_start(self):
		self.config_frame.EditEnable()
		self.cfgchange_frame.pack_forget()
		self.cfgconfirm_frame.pack()
	
	def _edit_cancel(self):
		self.config_frame.Restore()
		self.config_frame.EditDisable()
		self.cfgchange_frame.pack()
		self.cfgconfirm_frame.pack_forget()
	
	def _edit_commit(self):
		from ui import mainframe
		success, curr_data = self.config_frame.TryGetUIData()
		if not success:
			popup.showerror('错误', curr_data)
			return
		else:
			gamesection, selfdefine = curr_data
		modify = {}
		
		for k, v in gamesection.items():
			if not self.config_frame.cfgdata.Has(k):
				if str(v) != str(GAMECONFIG_DEFAULT_VALUE.get(k)):
					modify[k] = v
			elif self.config_frame.cfgdata.Get(k) != str(v):
				modify[k] = v
		
		if not modify and not selfdefine:
			self.config_frame.EditDisable()
			self.cfgchange_frame.pack()
			self.cfgconfirm_frame.pack_forget()
			mainframe.g_App.pages['服务器'].server_frame.operation_frame.CloseConfig(self.ip)
			return
		
		msg = '自定义修改请谨慎，\n确定要修改此配置文件吗？' if selfdefine else '你确定要修改此配置文件吗？'
		if not popup.double_confirm('', msg):
			return
			
		self.config_frame.cfgdata.Set(modify)
		if selfdefine:
			self.config_frame.cfgdata.SetBySection(*selfdefine)
		self.config_frame.EditDisable()
		self.cfgchange_frame.pack()
		self.cfgconfirm_frame.pack_forget()
		dataconfig = self.config_frame.cfgdata
		windowoperate.g_OptManager.AddOpt(self.ip, self.opt, dataconfig, callback=functools.partial(set_config_callback, self.ip))
		
def set_config_callback(ip, output):
	from ui import mainframe
	mainframe.g_App.pages['服务器'].server_frame.operation_frame.CloseConfig(ip)

