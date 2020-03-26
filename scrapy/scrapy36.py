from urllib import request
from bs4 import BeautifulSoup
import  re

url = "http://www.baidu.com"

rsp = request.urlopen(url)
# BeautifulSoup自动解码
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

print(soup.prettify())

print("==" * 20)
titles = soup.select("title")
print(titles[0])

print("==" * 20)
metas = soup.select("meta[content='always']")
print(metas[0])
print("==" * 20)

#
