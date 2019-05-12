from multiprocessing import Process, Pool
import os, time, random


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

if __name__=="__main__":
    '''
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')'''

    print('Parent process %s.' % os.getpid())
    p = Pool(100)
    for i in range(100):
        p.apply_async(long_time_task, args=(i,[1,2,3,4,5]))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')