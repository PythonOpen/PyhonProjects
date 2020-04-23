import urllib
import chardet
from urllib import request
'''
利用request下载页面
自动检测页面编码
'''
if __name__ == '__main__':
    url = "https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052092284&courseId=1004987028"

    rsp = request.urlopen(url)

    html = rsp.read()
    print(type(html))
    # 自动检测网页编码
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # cs.get("encoding", "utf-8")如果"encoding"的值不为空，则页面编码为'encoding'的值，
    # 否则编码方式默认为"utf-8"
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)