# -*- coding: gbk -*-
import json
import os
from game.command import *

SSH_USER			= 'test'
SSH_PASSWORD			= '123456'
APP_VERSION 			= [1, 0, 2]	#版本号,初始1.0.0
DEFAULT_CONSOLE_ID 		= '999999'
entry_font			= ('楷体', 12, 'bold')
CONFIG_FILE			= 'config.json'
UPLOAD_REMOTE_PATH		= "/home/test/sshtool_history/"
MAKEPY_CMD_FILE			= 'makepycmd.json'
TELNET_HISTORY_FILE		= 'telnethistory.json'
BATCH_HISTORY_FILE		= 'batchsaverecord.json'
BATCH_CONFIG_FILE		= 'batchset.json'
SELFDEFINE_CMD_HISTORY_FILE	= 'selfdefinecmd.json'
BATCH_SET_DATA			= ('桃手生效', '九州生效')
MAX_HISTORY_CNT			= 30

USERTYPE_QM_PISCES		= 1
USERTYPE_QM_YUJIAN		= 2
USERTYPE_QM_JIUZHOU		= 3
USERTYPE_CEHUA_PISCES		= 4
USERTYPE_CEHUA_YUJIAN_JIUZHOU	= 5
USERTYPE_DEVELOPER		= 6

USERTYPE_NAME = {
	USERTYPE_QM_PISCES		: "测试服-桃手",
	USERTYPE_QM_YUJIAN		: "测试服-御剑",
	USERTYPE_QM_JIUZHOU		: "测试服-九州",
	USERTYPE_CEHUA_PISCES		: "策划服-桃手",
	USERTYPE_CEHUA_YUJIAN_JIUZHOU	: "策划服-御剑九州",
	USERTYPE_DEVELOPER		: "开发服",
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
	OPTLABEL_DEFAULT	: '常用操作:',
	OPTLABEL_COMMON		: '公用操作:',
	OPTLABEL_JZ		: '九州:',
	OPTLABEL_PISCES		: '桃手:',
	OPTLABEL_AUTH		: '认证:',
	OPTLABEL_DATASRV	: 'DataSrv:',
}

#一个服可能有多重类型
SERVERTYPE_GAME		= 1
SERVERTYPE_KUAFU	= 2
SERVERTYPE_AUTH		= 4
SERVERTYPE_DATASRV	= 8

SERVERTYPE_2_NAME = {
	SERVERTYPE_GAME		: '游戏服',
	SERVERTYPE_KUAFU	: '跨服',
	SERVERTYPE_AUTH		: '认证服',
	SERVERTYPE_DATASRV	: 'datasrv服',
}

