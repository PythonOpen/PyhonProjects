import re
'''
findall
'''
s = r'\d+'
pattern = re.compile(s) # I标识忽略大小写

m = pattern.findall("i am 18 years old and 185 height")
print(m)

m = pattern.finditer("i am 18 years old and 185 height")
print(type(m))

for i in m:
    print(i.group())

