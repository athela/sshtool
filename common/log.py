# -*- coding: gbk -*-
import time
from define import *

ERROR_FILE_NAME		= 'error.log'
FILESIZE_MAX		= 50 * 1024
DEFAULT_UPLOAD_LOG_IP	= "192.168.1.123"

def LogError(msg):
	global g_ErrorFp
	if not g_ErrorFp:
		g_ErrorFp = open(ERROR_FILE_NAME, 'a')
	
	msg = time.strftime("[%Y-%m-%d %H:%M:%S] ", time.localtime(int(time.time()))) + msg + "\n"
	print(msg)
	g_ErrorFp.write(msg)
	g_ErrorFp.flush()
	
	if g_ErrorFp.tell() > FILESIZE_MAX:
		if UploadFile():				#上传
			print('upload success')
			g_ErrorFp.close()
			g_ErrorFp = open(ERROR_FILE_NAME, 'w')	#清空
		else:
			print('upload fail')

def UploadFile():
	from common import ssh
	ip = CONFIG_DATA.get("error_upload_ip", DEFAULT_UPLOAD_LOG_IP)
	client = ssh.GetSshClient(ip)
	if not client:
		return False
	return client.DoUploadFile(ERROR_FILE_NAME, UPLOAD_REMOTE_PATH, False)

def CloseFile():
	if g_ErrorFp:
		g_ErrorFp.close()

if 'g_ErrorFp' not in globals().keys():
	g_ErrorFp = None
