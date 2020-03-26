import re

s = r'([a-z]+) ([a-z]+)'
pattern = re.compile(s, re.I) # I标识忽略大小写

m = pattern.match("Hello world wide web")

# 表示返回匹配成功的整个子串
s = m.group(0)
print(s)

a = m.span(0) # 返回匹配成功，整个子串的跨度
print(a)

# 表示第一个分组的匹配成功的子串
s = m.group(1)
print(s)

# 表示第二个分组的匹配成功的子串
s = m.span(1)
print(s)

# 等价(m.group(1)，m.group(2))
s = m.groups()
print(s)


