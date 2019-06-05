from multiprocessing import Process, Pool
import os, time, random

'''
Python 多进程实现方式
'''

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def long_time_task(name, name2):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
    print(name2)


def fuc(list):
    print(sum(list))
l = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]

# 多进程的实现方式 1
def demo1():
    from concurrent.futures import ProcessPoolExecutor
    px = ProcessPoolExecutor(3)
    for i in range(3):
        px.submit(fuc, l[i])
        # px.submit(poolDemo, wn, wnList[i])  多参数
    px.shutdown(wait=True)

# 多进程的实现方式 2
def demo2():
    p = Pool(3)
    for i in range(3):
        p.apply_async(fuc, args=(l[i],))
        # p.apply_async(poolDemo, args=(wnL[i], wnList[i],))  多参数
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')

# 多进程的实现方式 3
def demo3():
    pr0 = []
    for i in range(3):
        p = Process(target=fuc, args=(l[i], ))
        pr0.append(p)
        p.start()
    for p in pr0:
        p.join()


if __name__ == "__main__":
    demo1()
    demo2()
    demo3()
    '''
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')'''

    '''
    print('Parent process %s.' % os.getpid())
    p = Pool(100)
    for i in range(100):
        p.apply_async(long_time_task, args=(i,[1,2,3,4,5]))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')'''