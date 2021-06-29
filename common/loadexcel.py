# -*- coding: gbk -*-
from define import *
import xlrd
import importlib

def OutputFile(filename, output, prefix = None, suffix = None):
	prefix = "#自动生成部分不要手动修改" if prefix is None else prefix
	suffix = "#以上为自动生成部分不要手动修改" if suffix is None else suffix
	
	f = open(filename, "r", encoding='gbk')
	msg = f.read()
	f.close()

	s = msg.find(prefix)
	e = msg.find(suffix, s)
	if s == -1 or e == -1:
		msg += "\n%s\n%s\n%s\n"%(prefix, output, suffix)
	else:
		msg = msg[:s+len(prefix)] + output + msg[e:]
	f = open(filename, "w", encoding='gbk')
	f.write(msg)
	f.close()

def LoadSheet(sheet, headers):
	content = []
	for row in range(1, sheet.nrows):
		col = 0
		row_data = []
		for h in headers:
			if type(h) is list:
				row_data.append(LoadList(sheet, 0, col, row, h))
				col += get_column_cnt(h)
			else:
				value = sheet.cell_value(row, col)
				if col == 0 and not value:
					break
				col += 1
				row_data.append(value)
		if len(row_data) > 0:
			content.append(row_data)
	return content

def LoadList(sh, base, col, row, headers):
	content = []
	for cur_row in range(row, sh.nrows):
		bd = sh.cell_value(cur_row, base)
		if cur_row > row and (not isinstance(bd, (str, )) or len(bd) > 0):
			return content

		x = col
		row_data = []
		for h in headers:
			if type(h) is list:
				row_data.append(LoadList(sh, col, x, cur_row, h))
				x += get_column_cnt(h)
			else:
				d = sh.cell_value(cur_row, x)
				if x == col and isinstance(d, (str, )) and len(d) == 0:
					break
				x += 1
				row_data.append(d)
		if len(row_data) > 0:
			content.append(row_data)
	return content
def get_column_cnt(h):
	cnt = 0
	for f in h:
		if type(f) is list:
			cnt += get_column_cnt(f)
		else:
			cnt += 1
	return cnt

def LoadExcel(filename):
	if not os.path.isfile(filename):
		print(filename, '不存在')
		return
	
	bk = xlrd.open_workbook(filename)
	sheet = bk.sheet_by_name("服务器列表")
	headers = ["服务器IP", "名字", "用户类别", "游戏服类别", ["指令类别", "指令字符串",], ["功能面板",], ['配置文件index', '配置文件名'], ['进程编号', '进程', '进程注释'], ]
	fd = LoadSheet(sheet, headers)
	d = "\nSERVER_DATA = {\n"
	user_type_dic = dict([(v, k) for k, v in globals().items() if isinstance(v, int) and k.startswith("USERTYPE_")])
	srv_type_dic = dict([(v, k) for k, v in globals().items() if isinstance(v, int) and k.startswith("SERVERTYPE_")])

	for ip, name, user_tp, srv_tp, cmds, opts, configs, processes in fd:
		user_tp = user_type_dic[int(user_tp)]
		srv_tp = int(srv_tp)
		srv_tp_str = ""
		for k, v in srv_type_dic.items():
			if k & srv_tp:
				srv_tp_str += "%s, "%v
		srv_cmds = ""
		for cmd, cmd_str, in cmds:
			if isinstance(cmd, str) and len(cmd.strip()) == 0:
				continue
			srv_cmds += "\t\t\t%d:\t\"%s\",\n"%(int(cmd), cmd_str.strip())
		srv_opts = ""
		for line, in opts:
			if isinstance(line, str) and len(line.strip()) == 0:
				continue
			srv_opts += "\t\t\t%s,\n"%line.strip(',')
		
		config_str = ""
		for cindex, configfile in configs:
			config_str += "\t\t\t%d:\t\"%s\",\n"%(cindex, configfile.strip())
		processes_str = ""
		for idx, progress, progress_note in processes:
			note = progress_note.strip()
			if note:
				processes_str += "\t\t\t(%d, \"%s\", \"%s\"),\n"%(int(idx), progress.strip(), note)
			else:
				processes_str += "\t\t\t(%d, \"%s\", None),\n" % (int(idx), progress.strip(), )
			
		d += "\t\"%s\": {\n"%ip
		d += "\t\t\"%s\":\"%s\",\n"%("name", name)
		d += "\t\t\"%s\":%s,\n"%("user_type", user_tp)
		d += "\t\t\"%s\":[%s],\n"%("srv_type", srv_tp_str)
		if srv_cmds:
			d += "\t\t\"%s\":\t{\n%s\t\t},\n"%("srv_cmds", srv_cmds)
		if srv_opts:
			d += "\t\t\"%s\":\t{\n%s\t\t},\n"%("srv_opts", srv_opts)
		if config_str:
			d += "\t\t\"%s\":\t{\n%s\t\t},\n"%("configfile", config_str)
		if processes_str:
			d += "\t\t\"%s\":\t[\n%s\t\t],\n"%("progresses", processes_str)
		d += "\t},\n"
	d += "}\n"
	OutputFile("game/serverlist.py", d)
	
	import game.serverlist
	importlib.reload(game.serverlist)

