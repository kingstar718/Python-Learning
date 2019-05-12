# -*- coding: UTF-8 -*-
import tkinter
from tkinter import *

''' # 例子1
top = tkinter.Tk()
top.mainloop()      # 进入消息循环
'''


# 例2
'''
root = Tk()  # 创建窗口对象的背景色

li = ['C', 'python', 'php', 'html', 'SQL', 'java']
movie = ['CSS', 'jQuery', 'Bootstrap']

listb = Listbox(root)  # 创建两个列表组件
listb2 = Listbox(root)

for item in li:
    listb.insert(0, item)  # 第一个小部件插入数据
for item in movie:
    listb2.insert(0, item)

listb.pack()  # 将小部件放置到主窗口中
listb2.pack()

root.mainloop()
'''

window = tkinter.Tk()
window.title("my window")
window.geometry('200x100')      # 使用x号  *不行

var = tkinter.StringVar()   # 文字变量储存器
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set("")

l = Label(
    window,
    # text = "Label Tk",       # 标签的文字
    textvariable = var,     # 使用 textvariable 替换 text, 因为这个可以变化
    bg = "blue",
    font = ("Arial", 12),        # 字体和字体大小
    width = 15, height = 2
)
l.pack()        # 固定窗口位置

b = tkinter.Button(
    window,
    text = "hit me",
    witdh = 15, height = 2,
    command = hit_me        # 点击按钮式执行的命令
)
b.pack()

window.mainloop()