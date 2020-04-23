from urllib import parse
from urllib import request
'''
掌握对url进行参数编码的方法
需要使用parse模块
'''
if __name__ == '__main__':
    url = "http://www.baidu.com/s?"
    wd = input("Input your keyword:")

    qs = {
        "wd": wd
    }
    # 转换url编码
    qs = parse.urlencode(qs)
    full_url = url+qs
    print(full_url)

    rsp = request.urlopen(full_url)

    html = rsp.read()
    html = html.decode()
    print(html)
