# -*- coding: utf-8 -*-
import tkinter as tk

'''
简单说明：
Entry是tkinter类中提供的的一个单行文本输入域，用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)。

什么时候用：
需要用户输入用户信息时，比如我们平时使用软件、登录网页时，用户交互界面让我们登录账户信息等时候可以用到。'''

window = tk.Tk()
window.title('My Window')
window.geometry('500x300')  # 这里的乘是小x

# 第4步，在图形界面上设定输入框控件entry并放置控件
e1 = tk.Entry(window, show='*', font=('Arial', 14))  # 显示成密文形式
e2 = tk.Entry(window, show=None, font=('Arial', 14))  # 显示成明文形式
e1.pack()
e2.pack()

# 第5步，主窗口循环显示
window.mainloop()