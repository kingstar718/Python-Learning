# encoding:UTF-8

"""
Python中使用线程有两种方式：函数或者用类来包装线程对象。
函数式：调用thread模块中的start_new_thread()函数来产生新线程。语法如下:
thread.start_new_thread ( function, args[, kwargs] )
"""
import threading


def function(i):
    print("function called by thread{} ".format(i))
    return

threads = []
for i in range(10):
    t =threading.Thread(target=function, args=(i, ))
    threads.append(t)
    #线程被创建之后并不会马上执行， 还需要手动调用start(), join() 让调用它的线程一直等到执行结束
    # （即阻塞他的主线程， t线程执行结束， 主线程才会继续执行）
    t.start()
    t.join()

# 创建两个线程
