import time
import threading as thread
import queue

semaphore=thread.Semaphore(3)
def func():
    if semaphore.acquire():
        for i in range(5):
            print(thread.currentThread().getName()+' get semaphore')
        time.sleep(15)
        semaphore.release()
        print(thread.currentThread().getName() + ' release semaphore')

for i in range(8):
        t1=thread.Thread(target=func)
        t1.start()

