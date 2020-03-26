import time,random,hashlib
from urllib import request, parse

'''
处理js加密代码
i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
sign = n.md5("fanyideskweb" + key + i + "n%A-rKaT5fb[Gy?;N5@Tj")
ts =  "" + (new Date).getTime()
'''


def getSalt():
    salt = int(time.time()*1000)+random.randint(0,10)
    return salt

def getMd5(v):
    md5 = hashlib.md5()
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()
    return sign


def getTs():
    Ts = int(time.time()*1000)
    return Ts


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    salt = str(getSalt())
    sign = getMd5("fanyideskweb" + key + salt + "n%A-rKaT5fb[Gy?;N5@Tj")
    ts= str(getTs())
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": "ab57a166e6a56368c9f95952de6192b5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }

    data = parse.urlencode(data).encode()

    headers = {
        "Accept": " application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": " zh-CN,zh;q=0.9",
        "Connection": " keep-alive",
        "Content-Length": len(data),
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": " OUTFOX_SEARCH_USER_ID=1912378164@61.140.239.208; OUTFOX_SEARCH_USER_ID_NCOO=1195959197.1059074; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abc-R9LqKRwNHgrjyPw9w; ___rl__test__cookies=1577712200873",
        "Host": " fanyi.youdao.com",
        "Origin": " http://fanyi.youdao.com",
        "Referer": " http://fanyi.youdao.com/",
        "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == "__main__":
    youdao("girl")