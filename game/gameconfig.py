# -*- coding: gbk -*-
from define import *
import configparser

'''
��Ϸ����
	proxyhost=192.168.1.113
	proxyport=9800
	grouphost=192.168.1.242
	groupport=9968

ս������
	proxyhost=192.168.51.39
	proxyport=9800
	combatserver=3
	combatport=9801	#���ø���

������ս������
	groupsrv=1
	centerhost=192.168.51.39
	centerport=9968

���ط���
	proxyserver=1
	proxyport=9800

���������أ�
	groupsrv=1
	groupport=9968
	centersrv=1
'''

#����
LOCAL_GAMECONFIG_TMP_FILE	= 'game.ini.swap'
DEFAULT_GAMECONFIG_FILE		= {
	OPT_GAMECONFIG				: 'game.ini',
	OPT_GAMECONFIG_PISCES			: 'game.ini',
	OPT_GAMECONFIG_JZ			: 'aquarius.ini',
	OPT_GAMECONFIG_CENTER 			: "game_center.ini",
	OPT_GAMECONFIG_BATTLE 			: "game_battle.ini",
	OPT_GAMECONFIG_CENTER_JZ		: "game_centerjz.ini",
	OPT_GAMECONFIG_BATTLE_JZ		: "game_battlejz.ini",
	OPT_GAMECONFIG_CENTER_PISCES 		: "game_center.ini",
	OPT_GAMECONFIG_BATTLE_PISCES 		: "game_battle.ini",
}

GAMECONFIG_DEFAULT_VALUE	= {	#�ⲿ��Ĭ��ֵ�Ǻ���Ϸ�ڴ���һ�µ�
	'testsrv'		: 0,
	'closerobot'		: 0,
	'open_time'		: 1301587200,
	'selfdefine_section'	: 'game',
	'centerhost'		: "127.0.0.1",
	'proxyhost'		: "127.0.0.1",
	'grouphost'		: "127.0.0.1",
	"centerport"		: 9968,
	"groupport"		: 9968,
	"proxyport"		: 9969,
	'groupsrv'		: 0,
	'proxyserver'		: 0,
	'centersrv'		: 0,
	'combatserver'		: 0,
}

COMBATSERVER_TYPE_KEY		= {	#����Ϸ�ڴ���һ��
	0 : '��',
	3 : '����ճ�',
	5 : 'ȫ�񾺼���',
	6 : '�·�ս',
	7 : '�����ս & ������',
}
COMBATSERVER_TYPE_NAME = dict(zip(COMBATSERVER_TYPE_KEY.values(), COMBATSERVER_TYPE_KEY.keys()))

class CConfigData(object):
	def __init__(self, output_str):
		self.cf = configparser.ConfigParser()
		self.cf.read_string(output_str)
	
	def GetFile(self):
		with open(LOCAL_GAMECONFIG_TMP_FILE, 'w') as f:	#����д
			self.cf.write(f)
		return LOCAL_GAMECONFIG_TMP_FILE
	
	def Set(self, modify):
		for k, v in modify.items():
			self.cf.set('game', str(k), str(v))
	
	def SetBySection(self, section, k, v):
		print(section, k, v)
		self.cf.set(section, str(k), str(v))
	
	def Del(self, k):
		if self.Has(k):
			self.cf.remove_option('game', k)
	
	def Has(self, k):
		return self.cf.has_option('game', k)
	
	def Get(self, k, usedefault=True):
		if self.cf.has_option('game', k):
			return self.cf.get('game', k)
		else:
			if usedefault:
				return GAMECONFIG_DEFAULT_VALUE.get(k)
	
	def GetSections(self):
		return self.cf.sections()
