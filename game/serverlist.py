# -*- coding: gbk -*-
from define import *

SERVER_DATA = {}
#�Զ����ɲ��ֲ�Ҫ�ֶ��޸�
SERVER_DATA = {
	"192.168.1.111": {
		"name":"���111-A",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.129": {
		"name":"���129",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.138": {
		"name":"���138",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.139": {
		"name":"���139",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.142": {
		"name":"���142",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.143": {
		"name":"ȫ��143",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.144": {
		"name":"ȫ��144",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.132": {
		"name":"ȫ��132",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.51.139": {
		"name":"����51.139",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.51.137": {
		"name":"���137",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.112": {
		"name":"���112",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_KUAFU, ],
		"srv_cmds":	{
			15:	"updateproxy.sh",
			16:	"rebootproxy.sh",
			17:	"traceproxy.sh",
			18:	"updatecombat.sh",
			19:	"rebootcombat.sh",
			20:	"tracecombat.sh",
			87:	"showcombat.sh",
			86:	"showproxy.sh",
		},
		"configfile":	{
			61:	"proxy.ini",
			62:	"combat.ini",
		},
		"progresses":	[
			(7, "chsrv32_proxy", None),
			(8, "chsrv32_combat", None),
		],
	},
	"192.168.51.132": {
		"name":"���132",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_KUAFU, ],
		"srv_cmds":	{
			15:	"updateproxy.sh",
			16:	"rebootproxy.sh",
			17:	"traceproxy.sh",
			18:	"updatecombat.sh",
			19:	"rebootcombat.sh",
			20:	"tracecombat.sh",
			87:	"showcombat.sh",
			86:	"showproxy.sh",
		},
		"configfile":	{
			61:	"proxy.ini",
			62:	"combat.ini",
		},
		"progresses":	[
			(7, "chsrv32_proxy", None),
			(8, "chsrv32_combat", None),
		],
	},
	"192.168.51.54": {
		"name":"���������54",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_KUAFU, ],
		"srv_cmds":	{
			15:	"updatescript.sh",
			16:	"rebootsrv.sh",
			17:	"tracelog.sh",
			86:	"showlog.sh",
		},
		"configfile":	{
			61:	"center.ini",
			62:	"battle.ini",
		},
	},
	"192.168.1.62": {
		"name":"���62-A",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
	},
	"192.168.1.185": {
		"name":"ȫ��185",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.186": {
		"name":"���186",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.189": {
		"name":"���189",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.65": {
		"name":"���65",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.190": {
		"name":"���190",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.51": {
		"name":"ȫ��51.51",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.131": {
		"name":"ȫ��51.131",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.135": {
		"name":"���51.135",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.138": {
		"name":"����51.138",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.66": {
		"name":"���66",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.51.130": {
		"name":"���51.130",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.51.36": {
		"name":"���36-A",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
	},
	"192.168.1.172": {
		"name":"ȫ��172",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.154": {
		"name":"�Զ�154",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.171": {
		"name":"���1.171",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.1.170": {
		"name":"���������170",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.1.122": {
		"name":"�߻�122",
		"user_type":USERTYPE_CEHUA_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.136": {
		"name":"�߻�136",
		"user_type":USERTYPE_CEHUA_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.157": {
		"name":"�߻�157",
		"user_type":USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.134": {
		"name":"�߻�134",
		"user_type":USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.123": {
		"name":"����",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"configfile":	{
			32:	"pisces.ini",
		},
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.51.37": {
		"name":"��ľ��",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.51.38": {
		"name":"��֮",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.162": {
		"name":"��ľ",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"configfile":	{
			32:	"pisces.ini",
		},
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.91": {
		"name":"����",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.155": {
		"name":"����",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"srv_cmds":	{
			7:	"switchto.sh os_jiuzhou;updatescript.sh",
			8:	"switchto.sh os_jiuzhou;rebootsrv.sh -9",
			11:	"switchto.sh os_taoshou;updatescript.sh",
			12:	"switchto.sh os_taoshou;rebootsrv.sh -9",
		},
		"srv_opts":	{
			3:[[7,8,33,76],  ],
			4:[[11,12,32,77],  ],
			6:[[6,5,3,4,], [39], [40],[73]],
		},
		"configfile":	{
			32:	"taoshou.ini",
			33:	"jiuzhou.ini",
		},
		"progresses":	[
			(1, "chsrv32_game", "switchto"),
		],
	},
	"192.168.51.62": {
		"name":"����",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"srv_cmds":	{
			7:	"switchto.sh os_jiuzhou;updatescript.sh",
			8:	"switchto.sh os_jiuzhou;rebootsrv.sh -9",
			11:	"switchto.sh os_taoshou;updatescript.sh",
			12:	"switchto.sh os_taoshou;rebootsrv.sh -9",
		},
		"srv_opts":	{
			3:[[7,8,33,76],  ],
			4:[[11,12,32,77],  ],
			6:[[6,5,3,4,], [39], [40],[73]],
		},
		"progresses":	[
			(1, "chsrv32_pisces", "switchto"),
		],
	},
	"192.168.51.64": {
		"name":"Bruce",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"srv_cmds":	{
			7:	"switchto.sh os_jiuzhou;updatescript.sh",
			8:	"switchto.sh os_jiuzhou;rebootsrv.sh -9",
			11:	"switchto.sh os_taoshou;updatescript.sh",
			12:	"switchto.sh os_taoshou;rebootsrv.sh -9",
		},
		"srv_opts":	{
			3:[[7,8,33,76],  ],
			4:[[11,12,32,77],  ],
			6:[[6,5,3,4,], [39], [40],[73]],
		},
		"progresses":	[
			(1, "chsrv32_pisces", "switchto"),
		],
	},
	"192.168.51.69": {
		"name":"�һ�",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"srv_cmds":	{
			7:	"switchto.sh os_jiuzhou;updatescript.sh",
			8:	"switchto.sh os_jiuzhou;rebootsrv.sh -9",
			11:	"switchto.sh os_taoshou;updatescript.sh",
			12:	"switchto.sh os_taoshou;rebootsrv.sh -9",
		},
		"srv_opts":	{
			3:[[7,8,33,76],  ],
			4:[[11,12,32,77],  ],
			6:[[6,5,3,4,], [39], [40],[73]],
		},
		"progresses":	[
			(1, "chsrv32_pisces", "switchto"),
		],
	},
	"192.168.51.34": {
		"name":"jasen",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"srv_cmds":	{
			7:	"updatejiuzhou.sh",
			8:	"rebootjiuzhou.sh -9",
			9:	"showjiuzhou.sh 2000",
			10:	"tracejiuzhou.sh",
			11:	"updatepisces.sh",
			12:	"rebootpisces.sh -9",
			13:	"showpisces.sh 2000",
			14:	"tracepisces.sh",
		},
		"configfile":	{
			32:	"game_pisces.ini",
			33:	"game_jiuzhou.ini",
		},
		"progresses":	[
			(1, "chsrv", None),
		],
	},
	"192.168.1.141": {
		"name":"1.141",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_KUAFU, SERVERTYPE_AUTH, ],
	},
	"192.168.51.56": {
		"name":"51.56",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.51.39": {
		"name":"51.39",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
}
#����Ϊ�Զ����ɲ��ֲ�Ҫ�ֶ��޸�
def GetConfigServerData():
	d = CONFIG_DATA.get("append_server_list", {})
	sample_ip = '0.0.0.0'
	if sample_ip in d:
		d.pop(sample_ip)
	return d

SERVER_DATA.update(GetConfigServerData())
def GetServerName(ip):
	return SERVER_DATA[ip]["name"]

def ClassifyServerData():
	d = {
		USERTYPE_QM_PISCES :[],
		USERTYPE_QM_YUJIAN :[],
		USERTYPE_QM_JIUZHOU :[],
		USERTYPE_CEHUA_PISCES :[],
		USERTYPE_CEHUA_YUJIAN_JIUZHOU: [],
		USERTYPE_DEVELOPER :[],
	}
	for ip, info in SERVER_DATA.items():
		d[info.get('user_type')].append(ip)
	return d
SERVER_DATA_CLASSIFIED = ClassifyServerData()

