from urllib import request, parse
import json

if __name__ == '__main__':
    baseurl = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': 'girl'
    }
    # 转换url编码
    data = parse.urlencode(data).encode('utf-8')
    print(type(data))

    headers = {
        "Content-Length": len(data)
    }

    req = request.Request(url=baseurl, data=data, headers=headers)

    # 有了headers.data.url，就可以发出请求了
    rsp = request.urlopen(req)
    json_data = rsp.read().decode('utf-8')
    print(type(json_data))
    print(json_data)

    # 把json字符串转化成字典
    json_data = json.loads(json_data)
    print(type(json_data))

    print(json_data)

    for item in json_data['data']:
        print(item['k'], "--", item['v'])