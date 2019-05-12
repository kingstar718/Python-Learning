import threading
import time


def first_function():
    print(threading.currentThread().getName() + str(" is Starting"))
    time.sleep(2)
    print(threading.currentThread().getName() + str(" is Starting"))
    return


def second_function():
    print(threading.currentThread().getName() + str(' is Starting '))
    time.sleep(2)
    print (threading.currentThread().getName() + str(' is Exiting '))
    return


def third_function():
    print(threading.currentThread().getName() + str(' is Starting '))
    time.sleep(2)
    print(threading.currentThread().getName() + str(' is Exiting '))
    return


if __name__ == "__main__":
    t1 = threading.Thread(name='first_function', target=first_function)
    t2 = threading.Thread(name='second_function', target=second_function)
    t3 = threading.Thread(name='third_function', target=third_function)
    t1.start()
    t2.start()
    t3.start()

    # 可以看到前3 个都是starting 都是互不影响的几乎都是同时执行的， 各自阻挡各自得线程2秒。 互不影响。