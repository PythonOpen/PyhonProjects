import time
import threading as thread

def loop1(in1):
    print('Start loop 1 at :',time.ctime())
    print("我是参数 ",in1)
    time.sleep(4)
    print('End loop 1 at :', time.ctime())

def loop2(in1,in2):
    print('Start loop 2 at :',time.ctime())
    print("我是参数 ",in1,"和参数 ",in2)
    time.sleep(2)
    print('End loop 2 at :', time.ctime())

def main():
    print('Starting at :',time.ctime())
    #()里为函数的参数
    t1=thread.Thread(target=loop1,args=("王老大",))
    t1.start()
    t2=thread.Thread(target=loop2,args=("王大鹏","王小鹏"))
    t2.start()
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
