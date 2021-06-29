# -*- coding: gbk -*-
import json
import os
from game.command import *

SSH_USER			= 'test'
SSH_PASSWORD			= '123456'
APP_VERSION 			= [1, 0, 2]	#�汾��,��ʼ1.0.0
DEFAULT_CONSOLE_ID 		= '999999'
entry_font			= ('����', 12, 'bold')
CONFIG_FILE			= 'config.json'
UPLOAD_REMOTE_PATH		= "/home/test/sshtool_history/"
MAKEPY_CMD_FILE			= 'makepycmd.json'
TELNET_HISTORY_FILE		= 'telnethistory.json'
BATCH_HISTORY_FILE		= 'batchsaverecord.json'
BATCH_CONFIG_FILE		= 'batchset.json'
SELFDEFINE_CMD_HISTORY_FILE	= 'selfdefinecmd.json'
BATCH_SET_DATA			= ('������Ч', '������Ч')
MAX_HISTORY_CNT			= 30

USERTYPE_QM_PISCES		= 1
USERTYPE_QM_YUJIAN		= 2
USERTYPE_QM_JIUZHOU		= 3
USERTYPE_CEHUA_PISCES		= 4
USERTYPE_CEHUA_YUJIAN_JIUZHOU	= 5
USERTYPE_DEVELOPER		= 6

USERTYPE_NAME = {
	USERTYPE_QM_PISCES		: "���Է�-����",
	USERTYPE_QM_YUJIAN		: "���Է�-����",
	USERTYPE_QM_JIUZHOU		: "���Է�-����",
	USERTYPE_CEHUA_PISCES		: "�߻���-����",
	USERTYPE_CEHUA_YUJIAN_JIUZHOU	: "�߻���-��������",
	USERTYPE_DEVELOPER		: "������",
}
SERVER_LABLES_BY_USER = {
	'test': [
		USERTYPE_QM_PISCES,
		USERTYPE_QM_YUJIAN,
		USERTYPE_QM_JIUZHOU,
		USERTYPE_CEHUA_PISCES,
		USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		USERTYPE_DEVELOPER,
	],
	'dev': [
		USERTYPE_DEVELOPER,
		USERTYPE_QM_PISCES,
		USERTYPE_QM_YUJIAN,
		USERTYPE_QM_JIUZHOU,
		USERTYPE_CEHUA_PISCES,
		USERTYPE_CEHUA_YUJIAN_JIUZHOU,
	],
	'cehua': [
		USERTYPE_CEHUA_PISCES,
		USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		USERTYPE_DEVELOPER,
		USERTYPE_QM_PISCES,
		USERTYPE_QM_YUJIAN,
		USERTYPE_QM_JIUZHOU,
	]
}

def LoadJsonFile(filename):
	if os.path.isfile(filename):
		with open(filename, 'r') as f:
			data = json.load(f)
			return data
	return {}

def WriteJsonFile(filename, filedata):
	if filedata:
		with open(filename, 'w') as f:
			json.dump(filedata, f, indent=8, ensure_ascii=False)

CONFIG_DATA = LoadJsonFile(CONFIG_FILE)
MAKEPY_CMD_DATA = LoadJsonFile(MAKEPY_CMD_FILE)
MAX_MESSAGE_LINE = max(CONFIG_DATA.get("max_line_number", 0), 2000)
TELNET_HISTORY_DATA = LoadJsonFile(TELNET_HISTORY_FILE)
BATCH_HISTORY_DATA = LoadJsonFile(BATCH_HISTORY_FILE)
BATCH_CONFIG_DATA = LoadJsonFile(BATCH_CONFIG_FILE)
SELFDEFINE_HISTORY_DATA = LoadJsonFile(SELFDEFINE_CMD_HISTORY_FILE)

def GetUserTypeSeq():
	user_type = CONFIG_DATA.get("user_department")
	if user_type in SERVER_LABLES_BY_USER:
		lst = SERVER_LABLES_BY_USER[user_type]
	else:
		lst = SERVER_LABLES_BY_USER['dev']
	return lst

OPTLABEL_AUTH		= 1
OPTLABEL_DATASRV	= 2
OPTLABEL_JZ		= 3
OPTLABEL_PISCES		= 4
OPTLABEL_DEFAULT	= 5
OPTLABEL_COMMON		= 6

OPTLABEL_NAME = {
	OPTLABEL_DEFAULT	: '���ò���:',
	OPTLABEL_COMMON		: '���ò���:',
	OPTLABEL_JZ		: '����:',
	OPTLABEL_PISCES		: '����:',
	OPTLABEL_AUTH		: '��֤:',
	OPTLABEL_DATASRV	: 'DataSrv:',
}

#һ���������ж�������
SERVERTYPE_GAME		= 1
SERVERTYPE_KUAFU	= 2
SERVERTYPE_AUTH		= 4
SERVERTYPE_DATASRV	= 8

SERVERTYPE_2_NAME = {
	SERVERTYPE_GAME		: '��Ϸ��',
	SERVERTYPE_KUAFU	: '���',
	SERVERTYPE_AUTH		: '��֤��',
	SERVERTYPE_DATASRV	: 'datasrv��',
}

