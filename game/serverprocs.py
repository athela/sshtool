# -*- coding: gbk -*-

from define import *
from game import serverlist
from game.command import *

#���̱��
PROC_GAME		= 1
PROC_GAME_PISCES	= 2
PROC_GAME_AQUARIUS	= 3
PROC_AUTH		= 4
PROC_REGISTER		= 5
PROC_DATASRV		= 6
PROC_CENTER		= 7
PROC_BATTLE		= 8
PROC_CENTER_PISCES	= 9
PROC_BATTLE_PISCES	= 10
PROC_CENTER_AQUARIUS	= 11
PROC_BATTLE_AQUARIUS	= 12

#�����ǳ�
PROC_NICKNAME = {
	PROC_GAME		: "��Ϸ",
	PROC_GAME_PISCES	: "����",
	PROC_GAME_AQUARIUS	: "����",
	PROC_AUTH		: "��֤auth",
	PROC_REGISTER		: "register",
	PROC_DATASRV		: "datasrv",
	PROC_CENTER		: "����",
	PROC_BATTLE		: "ս����",
	PROC_CENTER_PISCES	: "��������",
	PROC_BATTLE_PISCES	: "����ս����",
	PROC_CENTER_AQUARIUS	: "��������",
	PROC_BATTLE_AQUARIUS	: "����ս����",
}

#���̶�Ӧ�Ĳ�ѯ����·��ָ��
PROC_CODE_QUERY = {
	PROC_GAME		: OPT_UPDATECODE,
	PROC_GAME_PISCES	: OPT_UPDATE_PISCES,
	PROC_GAME_AQUARIUS	: OPT_UPDATE_JZ,
	PROC_AUTH		: OPT_UPDATE_AUTH_ONLY,
	PROC_DATASRV		: OPT_UPDATE_DATASRV,
	PROC_CENTER		: OPT_UPDATE_CENTER,
	PROC_BATTLE		: OPT_UPDATE_BATTLE,
	PROC_CENTER_PISCES	: OPT_UPDATE_CENTER_PISCES,
	PROC_BATTLE_PISCES	: OPT_UPDATE_BATTLE_PISCES,
	PROC_CENTER_AQUARIUS	: OPT_UPDATE_CENTER_JZ,
	PROC_BATTLE_AQUARIUS	: OPT_UPDATE_BATTLE_JZ,
}

#��ʵ������
PROC_ID_2_NAME = {
	PROC_GAME		: "chsrv32_game",
	PROC_GAME_PISCES	: "chsrv32_pisces",
	PROC_GAME_AQUARIUS	: "chsrv32_aquarius",
	PROC_AUTH		: "authsrv32",
	PROC_REGISTER		: "acc_main.py",
	PROC_DATASRV		: "datasrv32",
	PROC_CENTER		: "chsrv32_center",
	PROC_BATTLE		: "chsrv32_battle",
	PROC_CENTER_PISCES	: "chsrv32_center",
	PROC_BATTLE_PISCES	: "chsrv32_battle",
	PROC_CENTER_AQUARIUS	: "chsrv32_centerjz",
	PROC_BATTLE_AQUARIUS	: "chsrv32_battlejz",
}

def GetServerProcs(ip):	#��������ע�Ľ���
	def get_default_proc(srv_type, user_type):
		if srv_type is SERVERTYPE_GAME:
			if user_type is USERTYPE_DEVELOPER:
				return [PROC_GAME_PISCES, PROC_GAME_AQUARIUS]
			else:
				return [PROC_GAME ]
		elif srv_type is SERVERTYPE_KUAFU:
			if user_type is USERTYPE_DEVELOPER:
				return [PROC_CENTER_PISCES, PROC_BATTLE_PISCES, PROC_CENTER_AQUARIUS, PROC_BATTLE_AQUARIUS]
			else:
				return [PROC_CENTER, PROC_BATTLE]
		elif srv_type is SERVERTYPE_AUTH:
			return [PROC_AUTH, PROC_REGISTER]
		elif srv_type is SERVERTYPE_DATASRV:
			return [PROC_DATASRV]
		else:
			return []
	
	procs = serverlist.SERVER_DATA[ip].get("progresses", [])
	usertype = serverlist.SERVER_DATA[ip]["user_type"]
	ids = [v[0] for v in procs]
	has_game_prc = set(ids) & set([PROC_GAME, PROC_GAME_PISCES, PROC_GAME_AQUARIUS])
	
	for srvtp in serverlist.SERVER_DATA[ip]["srv_type"]:
		proc_ids = get_default_proc(srvtp,  usertype)
		for procid in proc_ids:
			if srvtp is SERVERTYPE_GAME and usertype is USERTYPE_DEVELOPER:
				if procid in [PROC_GAME, PROC_GAME_PISCES, PROC_GAME_AQUARIUS] and has_game_prc:
					continue
			if procid not in ids:
				procs.append((procid, PROC_ID_2_NAME[procid], None))
	
	return procs
