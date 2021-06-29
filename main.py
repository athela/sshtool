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
	1. 源码运行和打包使用较为稳定的 python3.8
		使用python3.9时， 打包出现 WARNING: lib not found: api-ms-win-core-path-l1-1-0.dll dependency of c:\python3\python39.dll，有些人的电脑上运行失败
	2. 依次安装模块
		pip install [paramiko|paramiko_expect|xlrd==1.2.0|pyinstaller|ConfigParser]
	3. 打包
		以在 main.py 目录下打包为例，打包命令：
			C:\python3\Scripts\pyinstaller.exe -D -p "..;..\common" -w -y --clean --specpath  ".pack" --workpath ".pack\build" --distpath ".pack\dist" -i "..\image.ico" -n sshtool main.py
			然后把目录下config.json拷到exe目录下[非必须]
		打包选项说明：
			-D, –onedir | 打包多个py文件, 在dist目录中生成很多依赖文件
			-p  DIR, –path=DIR | 设置导入路径(和使用PYTHONPATH效果相似)
				可以用路径分割符(Windows使用分号,Linux使用冒号)分割指定多个目录.
				也可以使用多个-p参数来设置多个导入路径，让pyinstaller自己去找程序需要的资源
			-w, –windowed,–noconsole | 使用Windows子系统执行. 当程序启动的时候不会打开命令行(只对Windows有效)
				当打包后的exe运行不起来时，可以去掉这个选项打包运行看哪里有问题
			-y	如果dist文件夹内已经存在生成文件，则不询问用户，直接覆盖
			–clean	在本次编译开始时，清空上一次编译生成的各种文件，默认不清除
			--specpath spec(规格)，打包的中间文件，整理的要打包的内容
			--workpath 生成的中间文件
			-–distpath 生成文件放在哪里
			-n 生成的.exe文件和.spec的文件名
			-i 为 main.exe指定图标
'''

def main():
	common.loadexcel.LoadExcel("服务器列表.xlsx")
	
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
		子线程不要直接输出到主界面，多线程时会输不出来
		主线程不要直接 结束子线程的tail，会卡界面
	'''
	main()
