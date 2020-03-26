from urllib import request, parse, error
import json
'''
    
'''
if __name__ == '__main__':
    url = 'https://www.renren.com/965187997/profile'

    rsp= request.urlopen(url)
    html = rsp.read().decode()
    print(html)

    with open('rsp.html','w')as f:
        f.write(html)