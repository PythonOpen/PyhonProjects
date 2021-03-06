from urllib import request, parse
from http import cookiejar

# 创建cookie的实例
cookie = cookiejar.CookieJar()
# 生成cookie请求管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 创建http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()
# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    # 此url需要重登陆form的action属性p中提取
    url = 'https://www.renren.com/PLogin.do'

    data = {
        "email": "13119144223",
        "password": "123456"
    }

    # 把数据进行编码
    data = parse.urlencode(data)
    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    login()
    print(cookie)
    for item in cookie:
        print(type(item))
        print(item)
        for i in dir(item):
            print(i)
