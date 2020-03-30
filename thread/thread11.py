import time
import threading as thread
import queue

lock1=thread.Lock()
lock2=thread.Lock()

def func_1():
    print("func_1 starting......")
    lock1.acquire()
    print("func_1 申请了 lock1......")
    time.sleep(2)
    print("func_1 等待 lock2......")
    lock2.acquire()
    print("func_1 申请了 lock2......")

    lock2.release()
    print("func_1 释放了 lock2......")

    lock1.release()
    print("func_1 释放了 lock1......")

    print("func_1 done......")

def func_2():
    print("func_2 starting......")
    lock2.acquire()
    print("func_2 申请了 lock2......")
    time.sleep(4)
    print("func_2 等待 lock1......")
    lock1.acquire()
    print("func_2 申请了 lock1......")

    lock1.release()
    print("func_2 释放了 lock1......")

    lock2.release()
    print("func_2 释放了 lock2......")

    print("func_2 done......")

if __name__=='__main__':
    print("主程序启动了")

    t1=thread.Thread(target=func_1,args=())
    t2 = thread.Thread(target=func_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("主程序启动了")
