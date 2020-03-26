from urllib import request
from bs4 import BeautifulSoup
import  re

url = "http://www.baidu.com"

rsp = request.urlopen(url)
# BeautifulSoup自动解码
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print("==" * 12)
tags = soup.find_all(name=re.compile('^me'), content="always")
for tag in tags:
    print(tag)
print("==" * 12)

