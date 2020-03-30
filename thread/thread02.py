import time
import _thread as thread

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
    thread.start_new_thread(loop1,("王老大",))
    thread.start_new_thread(loop2,("王大鹏","王小鹏"))
    print('All done at :', time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(1)
