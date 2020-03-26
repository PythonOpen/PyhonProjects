from urllib import request, parse, error
import json
'''
    使用代理访问一个网站
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener    
'''
if __name__ == '__main__':
    url = 'http://www.baidu.com'
    proxy = {'http': '101.95.115.196:8080'}
    Proxy_Handler = request.ProxyHandler(proxy)
    opener = request.build_opener(Proxy_Handler)
    request.install_opener(opener)

    # 现在访问url，则使用代理服务器
    try:
        rsp= request.urlopen(url)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print("HTTPError: {0}".format(e.reason))
        print("HTTPError: {0}".format(e))

    except error.URLError as e:
        print("URLError: {0}".format(e.reason))
        print("URLError: {0}".format(e))

    except Exception as e:
        print(e)