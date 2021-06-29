# -*- coding: gbk -*-
from define import *

SERVER_DATA = {}
#自动生成部分不要手动修改
SERVER_DATA = {
	"192.168.1.111": {
		"name":"体服111-A",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.129": {
		"name":"体服129",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.138": {
		"name":"体服138",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.139": {
		"name":"体服139",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.142": {
		"name":"体服142",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.143": {
		"name":"全服143",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.144": {
		"name":"全服144",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.132": {
		"name":"全服132",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.51.139": {
		"name":"测试51.139",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.51.137": {
		"name":"体服137",
		"user_type":USERTYPE_QM_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32", None),
		],
	},
	"192.168.1.112": {
		"name":"跨服112",
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
		"name":"跨服132",
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
		"name":"跨服竞技场54",
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
		"name":"体服62-A",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
	},
	"192.168.1.185": {
		"name":"全服185",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.186": {
		"name":"体服186",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.189": {
		"name":"体服189",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.65": {
		"name":"体服65",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.190": {
		"name":"体服190",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.51": {
		"name":"全服51.51",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.131": {
		"name":"全服51.131",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.135": {
		"name":"体服51.135",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.138": {
		"name":"测试51.138",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.66": {
		"name":"跨服66",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.51.130": {
		"name":"跨服51.130",
		"user_type":USERTYPE_QM_YUJIAN,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.51.36": {
		"name":"体服36-A",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, SERVERTYPE_AUTH, SERVERTYPE_DATASRV, ],
	},
	"192.168.1.172": {
		"name":"全服172",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.154": {
		"name":"自动154",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(1, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.171": {
		"name":"跨服1.171",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.1.170": {
		"name":"跨服竞技场170",
		"user_type":USERTYPE_QM_JIUZHOU,
		"srv_type":[SERVERTYPE_KUAFU, ],
	},
	"192.168.1.122": {
		"name":"策划122",
		"user_type":USERTYPE_CEHUA_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.136": {
		"name":"策划136",
		"user_type":USERTYPE_CEHUA_PISCES,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.157": {
		"name":"策划157",
		"user_type":USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.51.134": {
		"name":"策划134",
		"user_type":USERTYPE_CEHUA_YUJIAN_JIUZHOU,
		"srv_type":[SERVERTYPE_GAME, ],
	},
	"192.168.1.123": {
		"name":"朵朵服",
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
		"name":"伐木服",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.51.38": {
		"name":"云之",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.162": {
		"name":"二木",
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
		"name":"黑土",
		"user_type":USERTYPE_DEVELOPER,
		"srv_type":[SERVERTYPE_GAME, ],
		"progresses":	[
			(2, "chsrv32_pisces", None),
			(3, "chsrv32_aquarius", None),
		],
	},
	"192.168.1.155": {
		"name":"面条",
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
		"name":"阿瓜",
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
		"name":"灰灰",
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
#以上为自动生成部分不要手动修改
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

