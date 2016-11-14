#!/usr/bin/env python3.5
# coding = utf-8
# created by huang jian jun
'''
# python 的多进程借助 OS 模块
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac, windows no fork()
fd = os.fork()
if fd == 0:
    print("child process: %s is running, my parent process pid = %s " % (os.getpid(), os.getppid()))
else:
    print("father process: %s is running, created child process pid = %s " % (os.getppid(), pid))

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。
'''
# 由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象，
# 下面的例子演示了启动一个子进程并等待其结束：
'''
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))  # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
    print('Child process will start.')
    p.start()  # 用start()方法启动进程
    p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    print('Child process end.')
'''
'''
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print("child process %s (pid = %s) is going to run " % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print("parent process(%s) is running" % os.getppid())
    p = Pool(4)  # 设置进程池的进程的 MAX 值
    for i in range(1, 11): # 设置10个进程请求，进程池中的进程数最大为4，当池中没有空闲进程时，进程请求等待。
        result = p.apply_async(long_time_task, args=(i,))  # pool.apply_async()用来向进程池提交目标请求
    print('Waiting for all child processes done...')
    p.close()
    p.join()
    # pool.join()是用来等待进程池中的worker进程执行完毕，防止主进程在worker进程结束前结束。
    # result.successful()表示整个调用执行的状态，如果还有worker没有执行完，则会抛出AssertionError异常。
    if result.successful():
        print("successful done!")
    print('all child process done')

'''


# python 进程间通信
'''
Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''
'''
from multiprocessing import Process, Queue
import os, time, random

# 写数据进程执行的代码:
def write(q):
    print('Process: %s is going to write' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process: %s is going to read' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

'''
# python 的线程
'''
Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。
绝大多数情况下，我们只需要使用threading这个高级模块。
'''
'''
#  启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
import time, threading

def do_loop():
    n = 0
    print("threading %s is running······" % threading.current_thread().name)
    while n < 3:
        n += 1
        print("threading %s last %s " % (threading.current_thread().name, n))
        time.sleep(1)
    print("threading %s running ended!" % threading.current_thread().name)

if __name__=='__main__':
    print('thread %s is running...' % threading.current_thread().name) # 主线程 MainThread
    t = threading.Thread(target=do_loop, name='LoopThread') # 创建的新的线程 LoopThread
    t.start()
    t.join()
    print('thread %s ended.' % threading.current_thread().name)
'''
'''
由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，
Python的threading模块有个current_thread()函数，它永远返回当前线程的实例。
主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。
名字仅仅在打印时用来显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2·····
'''

'''
多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，
而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
# 来看看多个线程同时操作一个变量怎么把内容给改乱了：
'''
import threading
balance = 0 # 全局变量
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    #print("balance: %s" % balance)
# 先加后减，原理上blance = 0
def run_thread(n):
    for i in range(100000):
        change_it(n)

if __name__=="__main__":
    print("thread %s is running " % threading.current_thread().name)
    t1 = threading.Thread(target=run_thread, args=(8,))
    t2 = threading.Thread(target=run_thread, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("now the value of balance: %s " % balance)
'''
# 由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了。
'''
上述代码的运行结果：
                    thread MainThread is running
                    now the value of blance: 279

                    thread MainThread is running
                    now the value of blance: 0

                    thread MainThread is running
                    now the value of blance: 230
'''

'''
如果我们要确保balance计算正确，就要给change_it()上一把锁，当某个线程开始执行change_it()时，
我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，获得该锁以后才能改。
由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
创建一个锁就是通过threading.Lock()来实现：
当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止。
线程退出时，一定要释放锁， 否则其他线程会一直等待被占用的锁而成为死线程，所以我们用try...finally来确保锁一定会被释放。
'''

import threading
balance = 0 # 全局变量
lock = threading.Lock()  # 创建一个锁
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n
    #print("balance: %s" % balance)
# 先加后减，原理上blance = 0
def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()  # 线程请求锁
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

if __name__=="__main__":
    print("thread %s is running " % threading.current_thread().name)
    t1 = threading.Thread(target=run_thread, args=(8,))
    t2 = threading.Thread(target=run_thread, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("now the value of balance: %s " % balance)


