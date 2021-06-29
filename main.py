# -*- coding: gbk -*-
from ui import mainframe
import tkinter
import windowoperate
import windowmessage
import common.log
import common.ssh
import common.loadexcel

'''
readme:
	1. Դ�����кʹ��ʹ�ý�Ϊ�ȶ��� python3.8
		ʹ��python3.9ʱ�� ������� WARNING: lib not found: api-ms-win-core-path-l1-1-0.dll dependency of c:\python3\python39.dll����Щ�˵ĵ���������ʧ��
	2. ���ΰ�װģ��
		pip install [paramiko|paramiko_expect|xlrd==1.2.0|pyinstaller|ConfigParser]
	3. ���
		���� main.py Ŀ¼�´��Ϊ����������
			C:\python3\Scripts\pyinstaller.exe -D -p "..;..\common" -w -y --clean --specpath  ".pack" --workpath ".pack\build" --distpath ".pack\dist" -i "..\image.ico" -n sshtool main.py
			Ȼ���Ŀ¼��config.json����exeĿ¼��[�Ǳ���]
		���ѡ��˵����
			-D, �Conedir | ������py�ļ�, ��distĿ¼�����ɺܶ������ļ�
			-p  DIR, �Cpath=DIR | ���õ���·��(��ʹ��PYTHONPATHЧ������)
				������·���ָ��(Windowsʹ�÷ֺ�,Linuxʹ��ð��)�ָ�ָ�����Ŀ¼.
				Ҳ����ʹ�ö��-p���������ö������·������pyinstaller�Լ�ȥ�ҳ�����Ҫ����Դ
			-w, �Cwindowed,�Cnoconsole | ʹ��Windows��ϵͳִ��. ������������ʱ�򲻻��������(ֻ��Windows��Ч)
				��������exe���в�����ʱ������ȥ�����ѡ�������п�����������
			-y	���dist�ļ������Ѿ����������ļ�����ѯ���û���ֱ�Ӹ���
			�Cclean	�ڱ��α��뿪ʼʱ�������һ�α������ɵĸ����ļ���Ĭ�ϲ����
			--specpath spec(���)��������м��ļ��������Ҫ���������
			--workpath ���ɵ��м��ļ�
			-�Cdistpath �����ļ���������
			-n ���ɵ�.exe�ļ���.spec���ļ���
			-i Ϊ main.exeָ��ͼ��
'''

def main():
	common.loadexcel.LoadExcel("�������б�.xlsx")
	
	tk = tkinter.Tk()
	mainframe.WindowInit(tk)
	
	def tick():
		windowmessage.g_MsgHandler.Dequeue()
		tk.after(100, tick)
	tk.after(200, tick)# 200ms
	
	def close():
		windowoperate.g_OptManager.EndManager()
		common.log.CloseFile()
		common.ssh.Clear()
		tk.destroy()
		
	tk.protocol("WM_DELETE_WINDOW", close)
	tk.mainloop()

if __name__ == "__main__":
	'''
		���̲߳�Ҫֱ������������棬���߳�ʱ���䲻����
		���̲߳�Ҫֱ�� �������̵߳�tail���Ῠ����
	'''
	main()
