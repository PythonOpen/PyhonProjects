import re

s = r'\d+' # r标识后面为原生字符串，不需要转义
# 创建pattern对象
pattern = re.compile(s)
# 返回一个match对象
m = pattern.match("one12two34three5678")

print(type(m))
# 默认从头部开始查找，所以此次结果我饿哦None
print(m)

m = pattern.match("one12 6688two34three5678", 3, 10)
print(type(m))

print(m)

print(m.group())
print(m.group(0))
print(m.span(0))


