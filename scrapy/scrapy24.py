import requests
from urllib import parse
import json

if __name__ == '__main__':
    baseurl = 'https://fanyi.baidu.com/sug'
    data = {
        'kw': 'girl'
    }

    headers = {
        "Content-Length": str(len(data))
    }

    # 有了headers.data.url，就可以发出请求了
    rsp = requests.post(baseurl, data=data, headers=headers)

    print(rsp.text)
    print(rsp.json())

# for item in json_data['data']:
#    print(item['k'], "--", item['v'])

