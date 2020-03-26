from urllib import request
# 导入pythopn ssl处理模块
import ssl

# 利用非认证上下文环境替换认证的上下文环境
ssl._create_default_https_context = ssl._create_unverified_context
url = 'https://www.12306.cn/mormhweb/'
# 如果已经执行了login函数，则opener自动已经包含相应的cookie值
rsp = request.urlopen(url)
html = rsp.read().decode()
print(html)

