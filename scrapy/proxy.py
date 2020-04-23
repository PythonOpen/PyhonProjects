from urllib import request, error
import random
'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用random.choice

分析步骤:
1.构件代理群
2.每次访问，随机选取代理并执行
'''
proxy_list = [
    # 列表中存放的dict类型的元素
    {"https": "110.243.16.79:9999"},
    {"https": "122.241.225.227:60004"},
    {"https": "6223.68.190.130:8181"},
    {"https": "119.84.112.139:80"},
]

if __name__ == '__main__':
    # 使用代理的步骤
    # 1.设置代理地址
    # proxy = random.choice(proxy_list)
    # 2.创建ProxyHandler
    proxy_handler_list = []
    for proxy in proxy_list:
        proxy_handler = request.ProxyHandler(proxy)
        proxy_handler_list.append(proxy_handler)
    # 3.创建Opener
    opener_list = []
    for proxy_handler in proxy_handler_list:
        opener = request.build_opener(proxy_handler)
        opener_list.append(opener)

    url = "https://www.baidu.com"
    # 现在如果访问url，则使用代理服务器
    try:
        # 4.安装Opener
        opener = random.choice(opener_list)
        request.install_opener(opener)
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
