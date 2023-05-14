import tkinter as tk
import hashlib
import time
import base64
import requests
import time
from datetime import datetime

root = tk.Tk()
root.title("垃圾编码小公举")
root.config(background ="gray")
root.geometry('650x500+300+200')#设置主窗口的宽度为 450，高度为 400，同时窗口距离左边屏幕的距离为 300（以像素为单位）

#动态变量
imd5 = tk.StringVar()
ibase = tk.StringVar()
iurl = tk.StringVar()
itime = tk.StringVar()

#复制标签内容方法
def copy_label_text(i):
    label_text = i
    root.clipboard_clear()  # 清空剪贴板
    root.clipboard_append(label_text)  # 将文本内容添加到剪贴板
    print("已复制文本：", label_text)

#md5函数
def md5():
  hash = hashlib.md5()
  hash.update(Fmd52.get().encode(encoding='utf-8'))
  imd5.set('32位加密串小写：'+hash.hexdigest()+"\n"+'32位加密串大写：'+hash.hexdigest().upper()+"\n"+'16位加密串小写：'+hash.hexdigest()[8:24]+"\n"+'16位加密串大写：'+hash.hexdigest().upper()[8:24])
#base64编码
def enbase64(i):
    ibase.set(str(base64.b64encode(i.encode('utf-8')),encoding= 'utf-8'))
def debase64(i):
    ibase.set(str(base64.b64decode(i.encode('utf-8')),encoding= 'utf-8'))
#url编码--utf8
def enurl(i):
  iurl.set(requests.utils.quote(i))
def deurl(i):
  iurl.set(requests.utils.unquote(i))
#url编码--gb2312
def genurl(i):
  iurl.set(requests.utils.quote(i.encode('gb2312')))
def gdeurl(i):
  iurl.set(requests.utils.unquote(i,encoding='gb2312'))
#unix时间戳转换
def dtime(i):
  a = int(i)
  itime.set('秒：'+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(a))+'\n'+'毫秒：'+datetime.fromtimestamp(a/1000).strftime("%Y-%m-%d %H:%M:%S.%f"))
def etime(i):
  itime.set('秒：'+str(int(time.mktime(datetime.strptime(i, '%Y-%m-%d %H:%M:%S').timetuple())))+'\n'+'毫秒：'+str(int(round(time.mktime(datetime.strptime(i, '%Y-%m-%d %H:%M:%S').timetuple()) * 1000))))

#MD5
Fmd51 = tk.Label(anchor="center",bg="white",bd="0px",text="MD5算法：")
Fmd52 = tk.Entry(exportselection=0,selectbackground="gray")
Fmd53 = tk.Label(anchor="center",bg="white",bd="0px",text="结果：")
Fmd54 = tk.Label(anchor="center",textvariable=imd5)
Fmd55 = tk.Button(anchor="center",text="MD5算法",command=md5)
Fmd56 = tk.Button(text="复制结果",command=lambda: copy_label_text(Fmd54["text"]))

#base64编码
Fbase = tk.Label(anchor="center",bg="white",bd="0px",text="base64编码：")
Fbase1 = tk.Entry(exportselection=0,selectbackground="gray")
Fbase2 = tk.Label(anchor="center",bg="white",bd="0px",text="结果：")
Fbase3 = tk.Label(anchor="center",textvariable=ibase)
Fbase4 = tk.Button(anchor="center",text="base64编码",command=lambda: enbase64(Fbase1.get()))
Fbase5 = tk.Button(anchor="center",text="base64解码",command=lambda: debase64(Fbase1.get()))
Fbase6= tk.Button(text="复制结果",command=lambda: copy_label_text(Fbase3["text"]))

#url编码
Furl = tk.Label(anchor="center",bg="white",bd="0px",text="url编码：")
Furl1 = tk.Entry(exportselection=0,selectbackground="gray")
Furl2 = tk.Label(anchor="center",bg="white",bd="0px",text="结果：")
Furl3 = tk.Label(anchor="center",textvariable=iurl)
Furl4 = tk.Button(anchor="center",text="url编码-utf8",command=lambda: enurl(Furl1.get()))
Furl5 = tk.Button(anchor="center",text="url解码-utf8",command=lambda: deurl(Furl1.get()))
Furl6 = tk.Button(anchor="center",text="url编码-gb2312",command=lambda: genurl(Furl1.get()))
Furl7 = tk.Button(anchor="center",text="url解码-gb2312",command=lambda: gdeurl(Furl1.get()))
Furl8 = tk.Button(text="复制结果",command=lambda: copy_label_text(Furl3["text"]))

#unix时间戳转换
Ftime = tk.Label(anchor="center",bg="white",bd="0px",text="unix时间戳编码：")
Ftime1 = tk.Entry(exportselection=0,selectbackground="gray")
Ftime2 = tk.Label(anchor="center",bg="white",bd="0px",text="结果：")
Ftime3 = tk.Label(anchor="center",textvariable=itime)
Ftime4 = tk.Button(anchor="center",text="unix时间戳编码",command=lambda: etime(Ftime1.get()))
Ftime5 = tk.Button(anchor="center",text="unix时间戳解码",command=lambda: dtime(Ftime1.get()))
Ftime6= tk.Button(text="复制结果",command=lambda: copy_label_text(Ftime3["text"]))

#各模块布局控件置于主窗口 
Fmd51.grid(column=0,row=0)
Fmd52.grid(column=1,row=0)
Fmd53.grid(column=0,row=1)
Fmd54.grid(column=1,row=1)
Fmd55.grid(column=1,row=2)
Fmd56.grid(column=0,row=2)
Fbase.grid(column=0,row=3)
Fbase1.grid(column=1,row=3)
Fbase2.grid(column=0,row=4)
Fbase3.grid(column=1,row=4)
Fbase4.grid(column=1,row=5)
Fbase5.grid(column=2,row=5)
Fbase6.grid(column=0,row=5)
Furl.grid(row=6,column=0)
Furl1.grid(row=6,column=1)
Furl2.grid(row=7,column=0)
Furl3.grid(row=7,column=1)
Furl4.grid(row=8,column=1)
Furl5.grid(row=8,column=2)
Furl6.grid(row=8,column=3)
Furl7.grid(row=8,column=4)
Furl8.grid(row=8,column=0)
Ftime.grid(column=0,row=9)
Ftime1.grid(column=1,row=9)
Ftime2.grid(column=0,row=10)
Ftime3.grid(column=1,row=10)
Ftime4.grid(column=1,row=11)
Ftime5.grid(column=2,row=11)
Ftime6.grid(column=0,row=11)
root.mainloop()