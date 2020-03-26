from urllib import parse
from urllib import request
if __name__ == '__main__':
    url="http://www.baidu.com/s?"
    wd=input(("Input your keyword:"))

    qs={
        "wd":wd
    }
    # 转换url编码
    qs=parse.urlencode(qs)
    fullurl= url+qs
    print(fullurl)

    rsp=request.urlopen(fullurl)

    html=rsp.read()
    html=html.decode()
    print(html)
