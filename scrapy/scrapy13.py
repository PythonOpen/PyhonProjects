from urllib import request, parse, error
import json
'''
    
'''
if __name__ == '__main__':
    url = 'https://www.renren.com/965187997/profile'

    headers = {
        "Cookie": "anonymid=k4s64q3nyg36b6; depovince=GUZ; _r01_=1; ick_login=d0a4a0ca-fb3a-44b4-907e-e2c769931f33; t=13b14113e6d642ff72c92a3835b948276; societyguester=13b14113e6d642ff72c92a3835b948276; id=973199636; xnsid=aa17516a; jebecookies=81561232-c12a-4611-aef9-283b07d6fff9|||||; ver=7.0; loginfrom=null; jebe_key=929f6e95-fe91-4953-bf08-a128f3700fbc%7Ce516914498de6a5c8d3efc364a8d6c97%7C1577694314718%7C1%7C1577694510778"
    }
    req = request.Request(url, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()

    with open('rsp.html', 'w', encoding='utf-8')as f:
        f.write(html)
