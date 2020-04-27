from urllib import request, parse

"""
破解有道词典
"""


def youdao(key):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": "girl",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15878643244341",
        "sign": "3aefc1d99e663eaaa327a855f71431bf",
        "ts": "1587864324434",
        "bv": "acc97416ef67184f42e5a4a03c3d52ab",
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
        "Content-Length": " 237",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": " OUTFOX_SEARCH_USER_ID=1912378164@61.140.239.208; OUTFOX_SEARCH_USER_ID_NCOO=1195959197.1059074; DICT_UGC=be3af0da19b5c5e6aa4e17bd8d90b28a|; JSESSIONID=abc-R9LqKRwNHgrjyPw9w; ___rl__test__cookies=1577712200873",
        "Host": " fanyi.youdao.com",
        "Origin": " http://fanyi.youdao.com",
        "Referer": " http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()
    print(html)


if __name__ == "__main__":
    youdao("girl")

