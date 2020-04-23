from urllib import request

if __name__ == '__main__':
    url = "https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052092284&courseId=1004987028"
    rsp = request.urlopen(url)
    html = rsp.read()
    print(type(html))
    # 如果想把bytes内容转换成字符串，需要解码
    html = html.decode()
    print(html)