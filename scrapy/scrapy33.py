from urllib import request
from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
# BeautifulSoup自动解码
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

content = soup.prettify()
print(content)
print("==" * 12)
print("==" * 12)
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
soup.link.attrs['type'] = 'hahahahahha'
print(soup.link)
print("==" * 12)
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)
print(soup.title.string)
print("==" * 12)
print(soup.name)
print(soup.attrs)


