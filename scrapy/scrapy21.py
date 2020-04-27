from urllib import request
import json

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=60"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

req = request.Request(url=url, headers=headers)
rsp = request.urlopen(req)
data = rsp.read().decode()

data = json.loads(data)
print(data)
