from urllib import request

if __name__ == '__main__':
    url="https://study.163.com/course/courseLearn.htm?courseId=1004987028#/learn/video?lessonId=1052092284&courseId=1004987028"

    rsp=request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print("URL: {0}".format(rsp.geturl()))
    print("Info: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))
    html=rsp.read()
    html=html.decode()
