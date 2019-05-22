# -*- coding: utf-8 -*-

import tkinter as tk  # 使用Tkinter前需要先导入
from tkinter import messagebox

window = tk.Tk()    # 第1步，实例化object，建立窗口window
window.title('水质监测点布局')  # 第2步，给窗口的可视化起名字

window.geometry('500x300')  # 这里的乘是小x

var = tk.StringVar()

l = tk.Label(window, textvariable=var, bg='green', fg='white', font=('Arial', 12), width=30, height=2)
l.pack()

on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')
def loadInp():
    var.set("nihao")
    tk.messagebox.showinfo(title="Inp文件加载", message="加载完成")
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=hit_me).pack()
b2 = tk.Button(window, text='hit me', font=('Arial', 12), width=10, height=1, command=loadInp).pack()



# 第6步，主窗口循环显示
window.mainloop()

window.mainloop()