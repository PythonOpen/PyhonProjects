"""
使用多线程去播放两个播放列表，一个是movie,一个是music
_thread
threading
"""
# import time
# import _thread as thread
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(2)
#         else:
#             print("没有能播放的格式")
#
#
# def thread_run():
#     thread.start_new_thread(play, (movie_list,))
#     thread.start_new_thread(play, (music_list,))
#     while True:
#         time.sleep(10)
#
#
# if __name__ == "__main__":
#     thread_run()

"""
threading和_thread类似
threading 相对_thread来说更高级一点的线程包
"""
# import time
# import threading
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(2)
#         else:
#             print("没有能播放的格式")
#
#
# def thread_run():
#     t1 = threading.Thread(target=play, args=(movie_list,))
#     t2 = threading.Thread(target=play, args=(music_list,))
#     t1.start()
#     t2.start()
#
#
# if __name__ == "__main__":
#     thread_run()


# 类的方式去完成多线程
# import time
# import threading
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(2)
#         else:
#             print("没有能播放的格式")
#
#
# class MyThread(threading.Thread):
#     def __init__(self, playlist):
#         super().__init__()
#         self.playlist = playlist
#
#     def run(self):
#         play(self.playlist)
#
#
# if __name__ == "__main__":
#     m1 = MyThread(movie_list)
#     m2 = MyThread(music_list)
#     m1.start()
#     m2.start()


# 多进程 multiprocessing去完成
# import multiprocessing
# import time
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("你现在收看的是：{}".format(i))
#             time.sleep(2)
#         else:
#             print("没有能播放的格式")
#
#
# if __name__ == "__main__":
#     t1 = multiprocessing.Process(target=play, args=(movie_list,))
#     t2 = multiprocessing.Process(target=play, args=(music_list,))
#
#     t1.start()
#     t2.start()

"""
用协程的方式完成播放
"""
# import multiprocessing
# import asyncio
# import time
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']
#
#
# @asyncio.coroutine
# def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("now playing movie named:{}".format(i))
#             yield time.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("now playing music named:{}".format(i))
#             yield time.sleep(2)
#
#         else:
#             print("NO SUPPORTED")
#             yield time.sleep(1)
#
#
# loop = asyncio.get_event_loop()
# task = [play(movie_list), play(music_list)]
# loop.run_until_complete(asyncio.wait(task))
# loop.close()


"""
使用async def func()
"""
# import asyncio
# # import time
# movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
# music_list = ["周杰伦.mp3", "五月天.mp3"]
# movie_format = ['mp4', 'avi']
# music_format = ['mp3']


# @asyncio.coroutine
# async def play(playlist):
#     for i in playlist:
#         if i.split(".")[1] in movie_format:
#             print("now playing movie named:{}".format(i))
#             # yield time.sleep(3)
#             await asyncio.sleep(3)
#
#         elif i.split(".")[1] in music_format:
#             print("now playing music named:{}".format(i))
#             # yield time.sleep(2)
#             await asyncio.sleep(2)
#
#         else:
#             print("NO SUPPORTED")
#             # yield time.sleep(1)
#             await asyncio.sleep(1)
#
#
# loop = asyncio.get_event_loop()
# task = [play(movie_list), play(music_list)]
# loop.run_until_complete(asyncio.wait(task))
# loop.close()

"""
使用协程的概念，
达到以下的目的，
输入a,b,c,d四个参数，
打印出(a+b)*(c+d)的值，
假设a+b和c+d是一个耗时1s的IO操作
"""
import asyncio
import threading


async def sum(a, b):
    print("现在开始准备计算,current thread is {}".format(threading.currentThread()))
    r = int(a) + int(b)
    await asyncio.sleep(1)
    print("现在计算完了，current thread is {}".format(threading.currentThread()))
    return r

loop = asyncio.get_event_loop()
# asyncio.gather(func, func)为接收返回的结果
task = asyncio.gather(sum(1, 2), sum(3, 4))
loop.run_until_complete(task)
r1, r2 = task.result()
print(int(r1)*int(r2))
loop.close()
