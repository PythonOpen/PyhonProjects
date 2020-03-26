from urllib import request, parse
from http import cookiejar

# 创建cookie的实例
filename = "cookie.txt"
cookie = cookiejar.MozillaCookieJar(filename)
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
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
    # cookie.save()
    # 保存cookie到文件中
    # ignore_discard表示即使cookie将要被丢弃也要保存下来
    # ignore_expires表示如果该文件中cookie即使已经过期也保存
    cookie.save(ignore_discard=True, ignore_expires=True)

def getHomePage():
    url = 'https://www.renren.com/965187997/profile'

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)
    html = rsp.read().decode()

    with open('rsp.html', 'w', encoding='utf-8')as f:
        f.write(html)

if __name__ == '__main__':
    getHomePage()
