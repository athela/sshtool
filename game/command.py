# -*- coding: gbk -*-

SHOWLOG_MAX_LINE 		= 2000
TRACE_PROMPT			= 'password:'	#�ǿմ����κ��ַ��������ԣ��մ��ﲻ��Ч��

# OPT_ ����ֻ�����ģ���Ϊ���еĿ��ܱ������
OPT_SSH_WINDOW = 0
OPT_UPDATECODE = 1
OPT_REBOOTGAME = 2
OPT_SHOWLOG = 3
OPT_TRACELOG = 4
OPT_DATE = 5
OPT_DATE_QUERY = 6

OPT_UPDATE_JZ = 7
OPT_REBOOT_JZ = 8
OPT_SHOWLOG_JZ = 9
OPT_TRACELOG_JZ = 10

OPT_UPDATE_PISCES = 11
OPT_REBOOT_PISCES = 12
OPT_SHOWLOG_PISCES = 13
OPT_TRACELOG_PISCES = 14

OPT_UPDATE_CENTER = 15
OPT_REBOOT_CENTER = 16
OPT_TRACELOG_CENTER = 17

OPT_UPDATE_BATTLE = 18
OPT_REBOOT_BATTLE = 19
OPT_TRACELOG_BATTLE = 20

OPT_UPDATE_CENTER_JZ = 21
OPT_REBOOT_CENTER_JZ = 22
OPT_TRACELOG_CENTER_JZ = 23

OPT_UPDATE_BATTLE_JZ = 24
OPT_REBOOT_BATTLE_JZ = 25
OPT_TRACELOG_BATTLE_JZ = 26

OPT_MAKEPY = 27
OPT_UPDATE_MAP = 28
OPT_CLEARPYC = 29  # ɱ����,�建��
OPT_FORCEUPDATE = 30
OPT_GAMECONFIG = 31
OPT_GAMECONFIG_PISCES = 32
OPT_GAMECONFIG_JZ = 33
OPT_GAMECONFIG_QUERY = 34
OPT_GAMECONFIG_QUERY_PISCES = 35
OPT_GAMECONFIG_QUERY_JZ = 36
OPT_SHELL_SYSTEM_CMD = 39
OPT_SELF_DEFINE_SUDO = 40
OPT_REBOOT_AUTH = 41
OPT_UPDATE_AUTH = 42
OPT_SHOWLOG_AUTH = 43
OPT_SHOWLOG_REGISTER = 44
OPT_UPDATE_DATASRV = 45
OPT_REBOOT_DATASRV = 46
OPT_SHOWLOG_DATASRV = 47
OPT_QUERY_PROCS	= 48
OPT_QUERY_SWITCH = 49
OPT_QUERY_CODE_INFO = 50
OPT_QUERY_MEMERY = 51

OPT_UPDATE_CENTER_PISCES = 52
OPT_REBOOT_CENTER_PISCES = 53
OPT_TRACELOG_CENTER_PISCES = 54

OPT_UPDATE_BATTLE_PISCES = 55
OPT_REBOOT_BATTLE_PISCES = 56
OPT_TRACELOG_BATTLE_PISCES = 57

OPT_UPDATE_AUTH_ONLY	= 58
OPT_FORCEUPDATE_KUAFU_PISCES = 59
OPT_FORCEUPDATE_KUAFU_JZ = 60

OPT_GAMECONFIG_CENTER 			= 61
OPT_GAMECONFIG_BATTLE 			= 62
OPT_GAMECONFIG_CENTER_JZ		= 63
OPT_GAMECONFIG_BATTLE_JZ		= 64
OPT_GAMECONFIG_CENTER_PISCES 		= 65
OPT_GAMECONFIG_BATTLE_PISCES 		= 66
OPT_GAMECONFIG_CENTER_QUERY		= 67
OPT_GAMECONFIG_BATTLE_QUERY		= 68
OPT_GAMECONFIG_CENTER_JZ_QUERY		= 69
OPT_GAMECONFIG_BATTLE_JZ_QUERY		= 70
OPT_GAMECONFIG_CENTER_PISCES_QUERY	= 71
OPT_GAMECONFIG_BATTLE_PISCES_QUERY	= 72
OPT_BATCH_OPT_SET			= 73

OPT_DEBUG				= 74
OPT_DEBUG_WRITE				= 75
OPT_DEBUG_JZ				= 76
OPT_DEBUG_PISCES			= 77
OPT_DEBUG_CENTER_JZ			= 78
OPT_DEBUG_BATTLE_JZ			= 79
OPT_DEBUG_CENTER_PISCES			= 80
OPT_DEBUG_BATTLE_PISCES			= 81
OPT_DEBUG_CENTER			= 82
OPT_DEBUG_BATTLE			= 83
OPT_LABEL_CENTER			= 84
OPT_LABEL_BATTLE			= 85

OPT_SHOWLOG_CENTER			= 86
OPT_SHOWLOG_BATTLE			= 87
OPT_SHOWLOG_CENTER_JZ			= 88
OPT_SHOWLOG_BATTLE_JZ			= 89
OPT_SHOWLOG_CENTER_PISCES 		= 90
OPT_SHOWLOG_BATTLE_PISCES 		= 91

# ���̵߳��ڲ�ָ��
OPT_CLOSE_PAGE = 1000

OPT_NAME = {
	OPT_SHOWLOG				: '�鿴��־',
	OPT_SHOWLOG_JZ				: '�鿴������־',
	OPT_SHOWLOG_PISCES			: '�鿴������־',
	OPT_SHOWLOG_CENTER			: "�鿴������־",
	OPT_SHOWLOG_BATTLE			: "�鿴ս������־",
	OPT_SHOWLOG_CENTER_JZ			: "�鿴����������־",
	OPT_SHOWLOG_BATTLE_JZ			: "�鿴����ս������־",
	OPT_SHOWLOG_CENTER_PISCES 		: "�鿴����������־",
	OPT_SHOWLOG_BATTLE_PISCES 		: "�鿴����ս������־",
	
	OPT_DATE				: '��ʱ',
	OPT_DATE_QUERY				: '��ѯʱ��',
	OPT_MAKEPY				: '����',
	OPT_UPDATE_MAP				: '���µ�ͼ',
	OPT_CLEARPYC				: '�������',
	OPT_FORCEUPDATE				: 'ǿ��',
	OPT_GAMECONFIG_QUERY			: '��ѯ����',
	OPT_GAMECONFIG_QUERY_JZ			: '��ѯ��������',
	OPT_GAMECONFIG_QUERY_PISCES		: '��ѯ��������',
	OPT_GAMECONFIG_CENTER_QUERY		: '��ѯ��������',
	OPT_GAMECONFIG_BATTLE_QUERY		: '��ѯս��������',
	OPT_GAMECONFIG_CENTER_JZ_QUERY		: '��ѯ������������',
	OPT_GAMECONFIG_BATTLE_JZ_QUERY		: '��ѯ����ս��������',
	OPT_GAMECONFIG_CENTER_PISCES_QUERY	: '��ѯ������������',
	OPT_GAMECONFIG_BATTLE_PISCES_QUERY	: '��ѯ����ս��������',
	
	OPT_DEBUG				: 'debug',
	OPT_DEBUG_JZ				: 'debug_jz',
	OPT_DEBUG_PISCES			: 'debug',
	OPT_DEBUG_CENTER_JZ			: 'debug_center_jz',
	OPT_DEBUG_BATTLE_JZ			: 'debug_battle_jz',
	OPT_DEBUG_CENTER_PISCES			: 'debug_center',
	OPT_DEBUG_BATTLE_PISCES			: 'debug_battle',
	OPT_DEBUG_CENTER			: 'debug_center',
	OPT_DEBUG_BATTLE			: 'debug_battle',
	OPT_SHELL_SYSTEM_CMD			: 'ϵͳShell����',
	OPT_SELF_DEFINE_SUDO			: 'sudo����',
	OPT_REBOOT_AUTH				: '������֤',
	OPT_UPDATE_AUTH				: '������֤',
	OPT_SHOWLOG_AUTH			: '��֤��־',
	OPT_SHOWLOG_REGISTER			: 'Register��־',
	OPT_UPDATE_DATASRV			: '����Datasrv',
	OPT_REBOOT_DATASRV			: '����Datasrv',
	OPT_SHOWLOG_DATASRV			: 'Datasrv��־',
	
	OPT_UPDATECODE				: '���´���',
	OPT_UPDATE_JZ				: '���¾���',
	OPT_UPDATE_PISCES			: '��������',
	OPT_UPDATE_CENTER			: '��������',
	OPT_UPDATE_BATTLE			: '����ս����',
	OPT_UPDATE_CENTER_JZ			: '���ݸ�������',
	OPT_UPDATE_BATTLE_JZ			: '���ݸ���ս����',
	OPT_UPDATE_CENTER_PISCES		: '���ָ�������',
	OPT_UPDATE_BATTLE_PISCES		: '���ָ���ս����',
	
	OPT_REBOOT_JZ				: '��������',
	OPT_REBOOTGAME				: '������Ϸ',
	OPT_REBOOT_PISCES			: '��������',
	OPT_REBOOT_CENTER			: '��������',
	OPT_REBOOT_BATTLE			: '����ս����',
	OPT_REBOOT_CENTER_JZ			: '������������',
	OPT_REBOOT_BATTLE_JZ			: '��������ս����',
	OPT_REBOOT_CENTER_PISCES 		: '������������',
	OPT_REBOOT_BATTLE_PISCES 		: '��������ս����',
	
	OPT_TRACELOG				: '׷����־',
	OPT_TRACELOG_JZ				: '׷�پ�����־',
	OPT_TRACELOG_PISCES			: '׷��������־',
	OPT_TRACELOG_CENTER			: '������־',
	OPT_TRACELOG_BATTLE			: 'ս������־',
	OPT_TRACELOG_CENTER_JZ			: '����������־',
	OPT_TRACELOG_BATTLE_JZ			: '����ս������־',
	OPT_TRACELOG_CENTER_PISCES 		: '����������־',
	OPT_TRACELOG_BATTLE_PISCES 		: '����ս������־',
	
	OPT_FORCEUPDATE_KUAFU_PISCES		: 'ǿ�����ֿ��',
	OPT_FORCEUPDATE_KUAFU_JZ		: 'ǿ�����ݿ��',
	
	OPT_GAMECONFIG				: '��������',
	OPT_GAMECONFIG_JZ			: '���ľ�������',
	OPT_GAMECONFIG_PISCES			: '������������',
	OPT_GAMECONFIG_CENTER 			: '������������',
	OPT_GAMECONFIG_BATTLE 			: '����ս��������',
	OPT_GAMECONFIG_CENTER_JZ		: '���ľ�����������',
	OPT_GAMECONFIG_BATTLE_JZ		: '���ľ���ս��������',
	OPT_GAMECONFIG_CENTER_PISCES 		: '����������������',
	OPT_GAMECONFIG_BATTLE_PISCES 		: '��������ս��������',
}

OPT_BUTTON_NAME = {
	OPT_UPDATECODE				: "����",
	OPT_UPDATE_CENTER			: "����",
	OPT_UPDATE_BATTLE			: "����",
	OPT_UPDATE_JZ				: "����",
	OPT_UPDATE_PISCES			: "����",
	OPT_UPDATE_CENTER_JZ			: '����',
	OPT_UPDATE_BATTLE_JZ			: '����',
	OPT_UPDATE_CENTER_PISCES		: '����',
	OPT_UPDATE_BATTLE_PISCES		: '����',
	
	OPT_REBOOT_JZ				: '����',
	OPT_REBOOTGAME				: '����',
	OPT_REBOOT_PISCES			: '����',
	OPT_REBOOT_CENTER			: '����',
	OPT_REBOOT_BATTLE			: '����',
	OPT_REBOOT_CENTER_JZ			: '����',
	OPT_REBOOT_BATTLE_JZ			: '����',
	OPT_REBOOT_CENTER_PISCES		: '����',
	OPT_REBOOT_BATTLE_PISCES		: '����',
	
	OPT_TRACELOG				: '׷����־',
	OPT_TRACELOG_JZ				: '׷����־',
	OPT_TRACELOG_PISCES			: '׷����־',
	OPT_TRACELOG_CENTER			: '׷����־',
	OPT_TRACELOG_BATTLE			: '׷����־',
	OPT_TRACELOG_CENTER_JZ			: '׷����־',
	OPT_TRACELOG_BATTLE_JZ			: '׷����־',
	OPT_TRACELOG_CENTER_PISCES 		: '׷����־',
	OPT_TRACELOG_BATTLE_PISCES 		: '׷����־',
	
	OPT_SHOWLOG				: '��־',
	OPT_SHOWLOG_JZ				: '��־',
	OPT_SHOWLOG_PISCES			: '��־',
	OPT_SHOWLOG_CENTER			: "��־",
	OPT_SHOWLOG_BATTLE			: "��־",
	OPT_SHOWLOG_CENTER_JZ			: "��־",
	OPT_SHOWLOG_BATTLE_JZ			: "��־",
	OPT_SHOWLOG_CENTER_PISCES 		: "��־",
	OPT_SHOWLOG_BATTLE_PISCES 		: "��־",
	
	OPT_GAMECONFIG				: '����',
	OPT_GAMECONFIG_JZ			: '����',
	OPT_GAMECONFIG_PISCES			: '����',
	OPT_GAMECONFIG_CENTER 			: '����',
	OPT_GAMECONFIG_BATTLE 			: '����',
	OPT_GAMECONFIG_CENTER_JZ		: '����',
	OPT_GAMECONFIG_BATTLE_JZ		: '����',
	OPT_GAMECONFIG_CENTER_PISCES 		: '����',
	OPT_GAMECONFIG_BATTLE_PISCES 		: '����',
	
	OPT_DEBUG_JZ				: 'debug',
	OPT_DEBUG_CENTER_JZ			: 'debug',
	OPT_DEBUG_BATTLE_JZ			: 'debug',
	OPT_DEBUG_CENTER_PISCES			: 'debug',
	OPT_DEBUG_BATTLE_PISCES			: 'debug',
	OPT_DEBUG_CENTER			: 'debug',
	OPT_DEBUG_BATTLE			: 'debug',
	
	OPT_SHELL_SYSTEM_CMD			: "linux����س���Ч��:",
	OPT_SELF_DEFINE_SUDO			: "sudo����س���Ч��:",
	OPT_BATCH_OPT_SET			: "����������ʱ��",
	OPT_LABEL_CENTER			: "���أ�",
	OPT_LABEL_BATTLE			: "ս������",
	
	OPT_FORCEUPDATE_KUAFU_PISCES		: "ǿ��",
	OPT_FORCEUPDATE_KUAFU_JZ		: "ǿ��",
}
OPT_2_CMD = {
	OPT_UPDATECODE				: 'updatescript.sh',
	OPT_REBOOTGAME				: 'rebootsrv.sh -9',
	OPT_SHOWLOG				: 'showlog.sh %d' % SHOWLOG_MAX_LINE,
	OPT_TRACELOG				: 'tracelog.sh',
	OPT_DATE				: 'date -s \"%s\"',
	OPT_DATE_QUERY				: 'date "+%Y-%m-%d %H:%M:%S"',
	OPT_UPDATE_JZ				: 'updatejz.sh',
	OPT_REBOOT_JZ				: 'rebootjz.sh -9',
	OPT_SHOWLOG_JZ				: 'showjz.sh %d' % SHOWLOG_MAX_LINE,
	OPT_TRACELOG_JZ				: 'tracejz.sh',
	OPT_MAKEPY				: 'makepy.sh %s',
	OPT_UPDATE_MAP				: 'updatemap.sh',
	OPT_CLEARPYC				: 'clearpyc.sh',
	OPT_FORCEUPDATE				: 'forceupdate.sh',
	OPT_REBOOT_AUTH				: 'rebootauth.sh',
	OPT_UPDATE_AUTH				: 'updateauth.sh;updateregister.sh',
	OPT_UPDATE_AUTH_ONLY			: 'updateauth.sh',
	OPT_SHOWLOG_AUTH			: 'showauth.sh %d ' %SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_REGISTER			: 'showreglog.sh %d ' %SHOWLOG_MAX_LINE,
	OPT_UPDATE_DATASRV			: 'updatedatasrv.sh',
	OPT_REBOOT_DATASRV			: 'rebootdatasrv.sh',
	OPT_SHOWLOG_DATASRV			: 'showdatasrv.sh %d ' %SHOWLOG_MAX_LINE,
	OPT_QUERY_PROCS				: "ps -A -f |grep -w '%s' |grep -v grep |awk '{print $2}'",#-w��ȷƥ��
	OPT_QUERY_SWITCH			: "switchto.sh query",
	OPT_QUERY_MEMERY			: "free -m |grep Mem:|awk '{print $2}'",
	OPT_UPDATE_CENTER_PISCES 		: 'updatecenter.sh',
	OPT_REBOOT_CENTER_PISCES 		: 'rebootcenter.sh -9',
	OPT_TRACELOG_CENTER_PISCES		: 'tracecenter.sh',
	OPT_UPDATE_BATTLE_PISCES 		: 'updatebattle.sh',
	OPT_REBOOT_BATTLE_PISCES 		: 'rebootbattle.sh -9',
	OPT_TRACELOG_BATTLE_PISCES		: 'tracebattle.sh',
	OPT_UPDATE_CENTER_JZ			: 'updatecenterjz.sh',
	OPT_REBOOT_CENTER_JZ			: 'rebootcenterjz.sh -9',
	OPT_TRACELOG_CENTER_JZ			: 'tracecenterjz.sh',
	OPT_UPDATE_BATTLE_JZ			: 'updatebattlejz.sh',
	OPT_REBOOT_BATTLE_JZ			: 'rebootbattlejz.sh -9',
	OPT_TRACELOG_BATTLE_JZ			: 'tracebattlejz.sh',
	OPT_UPDATE_CENTER			: 'updatecenter.sh',
	OPT_REBOOT_CENTER			: 'rebootcenter.sh -9',
	OPT_TRACELOG_CENTER			: 'tracecenter.sh',
	OPT_UPDATE_BATTLE			: 'updatebattle.sh',
	OPT_REBOOT_BATTLE			: 'rebootbattle.sh -9',
	OPT_TRACELOG_BATTLE			: 'tracebattle.sh',
	OPT_FORCEUPDATE_KUAFU_PISCES		: 'forceupdate.sh',
	OPT_FORCEUPDATE_KUAFU_JZ		: 'forceupdatejz.sh',
	
	OPT_SHOWLOG_CENTER			: "showcenter.sh %d"%SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_BATTLE			: "showbattle.sh %d"%SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_CENTER_JZ			: "showcenterjz.sh %d"%SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_BATTLE_JZ			: "showbattlejz.sh %d"%SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_CENTER_PISCES 		: "showcenter.sh %d"%SHOWLOG_MAX_LINE,
	OPT_SHOWLOG_BATTLE_PISCES 		: "showbattle.sh %d"%SHOWLOG_MAX_LINE,
}
OPT_2_CMD[OPT_UPDATE_PISCES]	= OPT_2_CMD[OPT_UPDATECODE]
OPT_2_CMD[OPT_REBOOT_PISCES]	= OPT_2_CMD[OPT_REBOOTGAME]
OPT_2_CMD[OPT_SHOWLOG_PISCES]	= OPT_2_CMD[OPT_SHOWLOG]
OPT_2_CMD[OPT_TRACELOG_PISCES]	= OPT_2_CMD[OPT_TRACELOG]

TRACE_CMDS = [OPT_TRACELOG, OPT_TRACELOG_JZ, OPT_TRACELOG_PISCES, OPT_TRACELOG_CENTER, OPT_TRACELOG_BATTLE, OPT_TRACELOG_CENTER_JZ, OPT_TRACELOG_BATTLE_JZ, OPT_TRACELOG_CENTER_PISCES, OPT_TRACELOG_BATTLE_PISCES]
GAMECONFIG_CMD_2_QUERY = {
	OPT_GAMECONFIG		:OPT_GAMECONFIG_QUERY,
	OPT_GAMECONFIG_PISCES	:OPT_GAMECONFIG_QUERY_PISCES,
	OPT_GAMECONFIG_JZ	:OPT_GAMECONFIG_QUERY_JZ,

	OPT_GAMECONFIG_CENTER 			:OPT_GAMECONFIG_CENTER_QUERY	,
	OPT_GAMECONFIG_BATTLE 			:OPT_GAMECONFIG_BATTLE_QUERY	,
	OPT_GAMECONFIG_CENTER_JZ		:OPT_GAMECONFIG_CENTER_JZ_QUERY	,
	OPT_GAMECONFIG_BATTLE_JZ		:OPT_GAMECONFIG_BATTLE_JZ_QUERY	,
	OPT_GAMECONFIG_CENTER_PISCES 		:OPT_GAMECONFIG_CENTER_PISCES_QUERY,
	OPT_GAMECONFIG_BATTLE_PISCES 		:OPT_GAMECONFIG_BATTLE_PISCES_QUERY,
}
GAMECONFIG_QUERY_2_CMD = dict(zip(GAMECONFIG_CMD_2_QUERY.values(), GAMECONFIG_CMD_2_QUERY.keys()))
UPDATE_REVISION_CMDS = [OPT_UPDATECODE, OPT_UPDATE_JZ, OPT_UPDATE_PISCES, OPT_UPDATE_CENTER, OPT_UPDATE_BATTLE, OPT_UPDATE_CENTER_JZ, OPT_UPDATE_BATTLE_JZ, OPT_UPDATE_CENTER_PISCES, OPT_UPDATE_BATTLE_PISCES,
			OPT_UPDATE_AUTH, OPT_UPDATE_DATASRV, OPT_UPDATE_MAP]
IGNORE_OUTPUT_COMMAND = [OPT_QUERY_PROCS, OPT_QUERY_SWITCH, OPT_QUERY_CODE_INFO, OPT_QUERY_MEMERY]
FORCEUPDATE_NEED_PARAMETER_CMDS = [OPT_FORCEUPDATE_KUAFU_JZ, OPT_FORCEUPDATE_KUAFU_PISCES]
FORCEUPDATE_TWO_PATH_CMDS = [OPT_FORCEUPDATE_KUAFU_JZ, OPT_FORCEUPDATE_KUAFU_PISCES]
FORCEUPDATE_CMDS = [OPT_FORCEUPDATE_KUAFU_JZ, OPT_FORCEUPDATE_KUAFU_PISCES, OPT_FORCEUPDATE]
SHOWLOG_CMDS = [
	OPT_SHOWLOG_AUTH,
	OPT_SHOWLOG_REGISTER,
	OPT_SHOWLOG_DATASRV,
	OPT_SHOWLOG,
	OPT_SHOWLOG_JZ,
	OPT_SHOWLOG_PISCES,
	OPT_SHOWLOG_CENTER,
	OPT_SHOWLOG_BATTLE,
	OPT_SHOWLOG_CENTER_JZ,
	OPT_SHOWLOG_BATTLE_JZ,
	OPT_SHOWLOG_CENTER_PISCES,
	OPT_SHOWLOG_BATTLE_PISCES,
]
DEBUG_2_GAMECONFIG = {
	OPT_DEBUG		: OPT_GAMECONFIG,
	OPT_DEBUG_JZ		: OPT_GAMECONFIG_JZ,
	OPT_DEBUG_PISCES	: OPT_GAMECONFIG_PISCES,
	OPT_DEBUG_CENTER_JZ	: OPT_GAMECONFIG_CENTER_JZ,
	OPT_DEBUG_BATTLE_JZ	: OPT_GAMECONFIG_BATTLE_JZ,
	OPT_DEBUG_CENTER_PISCES	: OPT_GAMECONFIG_CENTER_PISCES,
	OPT_DEBUG_BATTLE_PISCES	: OPT_GAMECONFIG_BATTLE_PISCES,
	OPT_DEBUG_CENTER	: OPT_GAMECONFIG_CENTER,
	OPT_DEBUG_BATTLE	: OPT_GAMECONFIG_BATTLE,
}

def get_selfinput_commandstr(input, opt):#���������ָ��
	command = input
	if opt is OPT_SELF_DEFINE_SUDO:
		lst = [c.strip() for c in command.split()]
		tmpstr = ''.join(lst[1:])
		if lst[0] == 'sudo' and tmpstr.startswith('-ugame'):
			command = "sudo -ugame -S -p '' " + command[4:].strip()[2:].strip()[4:]
		elif lst[0] == 'sudo' and not tmpstr.startswith('-ugame'):
			command = "sudo -S -p '' " + command[4:].strip()
		else:
			return
	else:
		if command == 'top' or command.startswith('top '):
			command = 'top -b -n 1'
	return command

def GetCommandStr(ip, opt, args):
	from game import serverlist
	from game import gameconfig
	
	def get_cmd_by_opt(opt):
		cmd = serverlist.SERVER_DATA[ip].get("srv_cmds", {}).get(opt)
		if cmd is None:
			cmd = OPT_2_CMD.get(opt)
		return cmd
	
	use_tail = False
	if opt in [OPT_SHELL_SYSTEM_CMD, OPT_SELF_DEFINE_SUDO]:
		command = get_selfinput_commandstr(args[0], opt)
	elif opt in GAMECONFIG_QUERY_2_CMD:
		tmpopt = GAMECONFIG_QUERY_2_CMD[opt]
		configfile = serverlist.SERVER_DATA[ip].get("configfile", {}).get(tmpopt, gameconfig.DEFAULT_GAMECONFIG_FILE[tmpopt])
		command = "cat %s" % configfile
	else:
		cmd = get_cmd_by_opt(args[0] if opt is OPT_QUERY_CODE_INFO else opt)
		if cmd is None:
			return None, use_tail
			
		if opt is OPT_QUERY_PROCS:
			command = cmd % args[0]
		elif opt in [OPT_DATE_QUERY, OPT_QUERY_MEMERY]:
			command = cmd
		elif opt is OPT_DATE:
			cmd = cmd % args[0]
			command = "sudo -S -p '' %s" % cmd
		elif opt in TRACE_CMDS + FORCEUPDATE_CMDS:
			use_tail = True
			if opt in FORCEUPDATE_NEED_PARAMETER_CMDS:
				cmd = cmd + " %s" % args[0]
			command = "sudo -ugame -S -p %s %s" % (TRACE_PROMPT, cmd)
		elif opt is OPT_MAKEPY:
			arg = args[0]
			if arg.find(',') != -1:
				cmds = [cmd % makestr for makestr in arg.split(',')]
				command = ["sudo -ugame -S -p '' %s" % c for c in cmds]
			else:
				cmd = cmd % arg
				if arg == 'query':
					command = "sudo -ugame -S -p '' %s" % cmd
				else:
					use_tail = True
					command = "sudo -ugame -S -p %s %s" % (TRACE_PROMPT, cmd)
		else:
			arg = ""
			if opt in UPDATE_REVISION_CMDS + SHOWLOG_CMDS:
				if len(args) == 1:
					arg = args[0]
			
			if opt is OPT_QUERY_CODE_INFO:
				cmd = cmd + " query"
			
			if ';' in cmd:
				command = ["sudo -ugame -S -p '' %s %s" % (c, arg) for c in cmd.split(';')]
			else:
				command = "sudo -ugame -S -p '' %s %s" % (cmd, arg)
	return command, use_tail
