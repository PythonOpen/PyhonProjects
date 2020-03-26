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
        "salt": "15777122008771",
        "sign": "f9552aa61692d67290eb7cf12edf5a5c",
        "ts": "1577712200877",
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
        "Content-Length": " 237",
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

