import re
'''
findall
'''
hello = u'您好，世界!'
s = r'[\u4e00-\u9fa5]+'
pattern = re.compile(s)

m = pattern.findall(hello)
print(m)


