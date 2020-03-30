# Python
- 爬虫分类
    - 通用爬虫
    - 专用爬虫（聚焦爬虫）
    
- Python网络包简介
    - Python2.x:urllib,urllib2,urllib3,httplib,httplib2,requests
    - Python3.x:urllib,urllib3,httplib2,requests
    
# 2.urllib
- 包含模块
    - urllib.request:打开和读取urls
    - urllib.error:
    - urllib.parse:包含解析url的方法
    - urllib.robotparse:解析robot.txt
    
- request.data的使用
    - 访问网络的两种方法
        - get
        - post
            - 使用post，意味着HTTP的请求头可能需要更改：
                - Content-Type:application/x-www.form-urlencode
                - Cotent-length:数据长度
                - 简而言之，一般更改请求方法，请注意其他请求头部信息相适应
            - urllib.parse.urlencode可以字符串自动转换换成上面的
            - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太好哦啊用了
            - 需要利用request.Request
            
        - urllib.error
            - URLError产生的原因：
                - 没网
                - 服务器链接失败
                - 是OSError的子类
                - ...
            - HTTPError, 是URLError的一个子类
            - 两者区别：
                - HTTPError是对应的HTTP请求的返回码错误，如果返回错误码是400以上的，则引发HTTPError
                - URLError对应的一般是网络出现问题，包括url问题
                - 关键区别：OSError-URLError-HTTPError
                
    - UserAgent
        - UserAgent:用户代理，简称UA，属于heads的一部分，服务器通过UA来判断访问者身份
        - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包
        - Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36
    - 设置UA可以通过两种方式：
        - headers
        - add_header
                    
- ProxyHandler处理（代理服务器）
    - 使用代理IP.是爬虫的常用手段
    - 获取代理服务器的地址：
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，歹意一定要很多很多
    - 基本使用步骤：
        1. 设置代理地址
        2. 创建ProxyHandler
        3. 创建Opener
        4. 安装Opener
                
- cookie & session
    - 由于http协议的无记忆性，人们为了弥补这个缺憾，所采用的一个补充协议
    - cookie是发放给用户（http浏览器）的一段信息，session保存到服务器上
    
- cookie和session的区别
    - 存放位置不同
    - cookie不安全
    - seesion会保存在服务器上一定时间，会过期
    - 单个cookie保存数据不超过4k，很多浏览器限制一个站点最多保存20个
    
- session的存放位置
    - 存在服务器端
    - 一般情况，seesion是放在内存中或者数据库中
- 使用cookie登录    
    - 直接把cookie复制下来，然后手动放入请求头，案例scrapy13
    - http模块包含一些关于cookie的模块，通过他们我们可以自动使用cookie
        - CookieJar
            - 管理存储cookie,向传出的http请求添加cookie
            - cookie存储在内存中，CookieJar实例回收后cookie将消失
        - FileCookieJar(filename, delayload=None, policy=None)
            - 使用文件管理cookie
            - filename是保存cookie的文件
        - MozillaCookieJar(filename, delayload=None, policy=None)
            - 创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
        - LwpCookieJar(filename, delayload=None, policy=None)
            - 创建与libwww-perl标准兼容的Set-Cookie3格式的FileCookieJar实例
        - 他们的关系是：CokieJar-->FileCookieJar-->MozillarCookieJar & LwpCookieJar
    - 利用cookieJar访问人人网，案例14   
        - 自动使用cookie登录，大致流程
        - 打开登录页面后自动通过用户名密码登录
        - 自动提取反馈回来的cookie
        - 利用提取的cookie登录隐私页面 
        
    - cookie的属性
        - name: 名称
        - value: 值
        - domin: 可以访问此cookie的域名
        - path: 可以发批文此cookie的页面路径
        - expires:过期时间
        - size: 大小
        - Http字段
    - cookie保存在filename
    - cookie的读取
    
- SSL
    - SSL证书就是指遵守SSL安全套阶层协议的服务器数字证书（SercureSocketLayer）
    - 美国网景公司开发
    - CA(CertifacateAuthority)是数字证书认证中心，是发放，管理，废除数字证书的收信人的第三方机构
    - 遇到不信任的SL证书，需要单独处理，案例18
    
- js加密
    - 有的反爬虫策略采用js对需要传输的数据进行加密处理（通常是mde5值）
    - 经过加密，传输的就是密文，但是
    - 加密函数或者过程一定是在浏览器完成，也就是一定会把代码（js代码）暴露给使用者
    - 通过阅读加密算法，就可以模拟出加密过程，从而达到破解
    - 案例19,20
    
- ajax
    - 异步请求
    - 一定会有url，请求方法，可能有数据
    - 一般使用json格式
    - 案例，爬豆瓣电影 案例21
    
# Requests-献给人类
- HTTP for Humans,更简洁更友好
- 继续了urllib的所有特征
- 底层使用是urllib3
- 开源地址：https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- get请求
    - requests.get(url)
    - requests.request("get",url)
    - 可以带有heads和parmas参数
    案例22
- get 返回内容
    - 案例23
    
- post
    - rsp = requests.post(url,data=data)
    - data, headers要求dict类型
    - 案例24
    
- proxy
    proxies = {
        "http":"address of proxy" 
    }
    rsp = requests.request("get", "hrrp:xxxx", proxies=proxies)
    - 代理有可能报错，如果使用人数多，考虑安全问题，可能会被强行关闭
    
- 用户验证
    - 代理验证
        - 可能需要使用HTTP absic Auth,可以这样
        - 格式为 用户名：密码@代理地址
        - proxy = {"http": "china:123456@192.168.1.123:4444"}
        - rsp = requests.get("http://baidu.com", proxies=proxy)
    
- web客户端验证
    - 如果遇到web客户端验证，需要添加auth= （用户名，密码）
        - antu("test1", "123456") # 授权信息
        rsp = requests.get("http://baidu.com", auth=auth)
        
- cookie
     - requests可以自动处理cookie信息
     - rsp = requests.get("http://xxxxxx")
     - cookiejar = rsp.cookies
     - cookiejar转换成字典
     - cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    
- session
    - 跟服务器端session不是一个东东
    - 模拟一次会话，从客户端浏览器链接服务器开始，到客户端浏览器断开
    - 能让我们跨请求时保持某些参数，比如在同一个session实例发出的 所有请求之间保持cookie
        # 创建session对象，可以保持cookie值
        - ss = requests.session()
        - headers = {"User-Agent":"xxxxxxxxxxxxxxxxxx"}
        - data = {"name":"xxxxxxxxx"}
        # 此时，由创建的session管理请求,负责发出请求
        ss.post("http://www.baidu.com", data=data, headers=headers)
        
    - https请求验证ssl证书
        - 参数verify负责标识是否需要验证ss证书，默认是True
        - 如果不需要验证ssl证书，直接设置成false表示关闭
            - rsp = requests.get("https://www.baidu.com", verify=False)
            - 如果是verfy=True访问12306，会报错，因为证书有问题
        
    