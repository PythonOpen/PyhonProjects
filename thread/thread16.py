from time import  sleep,ctime
import multiprocessing
import threading as thread
import queue

def clock(interval):
    while True:
        print("The time is %s" %ctime())
        sleep(interval)

if __name__ == '__main__':
    p=multiprocessing.Process(target=clock,args=(5,))
    p.start()