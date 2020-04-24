from urllib import request, parse
# 负责处理json格式
import json
'''
大致流程是:
1.利用data构造内容，然后urlopen打开
2.返回一个json格式的结果
3.结果就应该是girl的释义
1.打开F12
2.尝试输入单词girl，发现每敲一个字母后都有请求
3.请求地址是http://fanyi.baidu,com/sug
4.利用NetWork-All-Headers查看，发现FromData的值是kw:girl
5.检查返回内容格式，发现返回的是json格式内容==>需要利用json包
'''

if __name__ == '__main__':
    baseurl = 'https://fanyi.baidu.com/sug'
    word = input("请输入一个单词:")
    data = {
        'kw': word
    }
    # 转换url编码
    data = parse.urlencode(data).encode('utf-8')
    print(type(data))

    # headers = {
    #     "Content-Length": len(data)
    # }

    # 有了headers.data.url，就可以发出请求了
    rsp = request.urlopen(baseurl, data=data)
    json_data = rsp.read().decode('utf-8')
    print(type(json_data))
    print(json_data)

    # 把json字符串转化成字典
    json_data = json.loads(json_data)
    print(type(json_data))
    print(json_data)

    for item in json_data['data']:
        print(item['k'], "--", item['v'])
