import re
'''
search
'''
s = r'\d+'
pattern = re.compile(s) # I标识忽略大小写

m = pattern.search("one12two34three56")

print(m.group())

m = pattern.search("one12two34three56",10,40)

print(m.group())


