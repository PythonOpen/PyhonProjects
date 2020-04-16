import re
# 匹配一行文字中所有开头的字母
# s = 'i l.ove you 66but you 你don\'t love me\n'
#
# # \b\w findall
# # \b\w为匹配首字符，\w\b匹配尾字母
# content1 = re.findall(r'\b\w', s)
# content2 = re.findall(r'\w\b', s)
# print(content1)
# print(content2)

# # 匹配一行文字中所有数字开头的
# s1 = 'i 22love 33you but you66 88don\'t 9love me'
# # \d
# # \b\d为匹配首数字，\d\b匹配尾数字
# content1 = re.findall(r'\b\d', s1)
# content2 = re.findall(r'\d\b', s1)
# print(content1)
# print(content2)

# # 匹配只含数字和字母的行
# s2 = 'i 22love 33..you\n but yo.u66\n 88don\'t 9l.ove \nmsf354466e'
# """
# “.”的作用是匹配除“\n”以外的任何字符，也就是说，它是在一行中进行匹配
# ^只匹配字符串的开头，$只匹配字符串结尾,.不匹配换行符
# re.S做的事情是: 它表示 “.” 的作用扩展到整个字符串，包括“\n”
# re.M做的事情是: 让^匹配每行的开头，$匹配每行的结尾,影响^和$
#
# """
# content1 = re.findall(r'\w+$', s2, re.M)
# content2 = re.findall(r'^\w+', s2, re.M)
# content3 = re.findall(r'.\w+', s2, re.S)
# # 后面加?为非贪婪匹配，尽可能少
# content4 = re.findall(r'.\w+?', s2, re.S)
# print(content1)
# print(content2)
# print(content3)
# print(content4)

# 写一个正则表达式，使其能匹配一下字符 'bit','bat','but','bat','hit','but'
# s3 = "'bit','bat','but','bat','hit','but'"
# content = re.findall(r'..t', s3)
# print(content)

# 提取每行中完整的年月日和时间
# s3 = "se2332 1987-10-12 05:02:00 jskdfmkasf 2018-10-20 09:48:20"
# content = re.findall(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', s3)
# print(content)

# 提取电子邮件格式
# s4 = 'xxxxx@gmail.com xxxx@qq.com baidu.com 999.com jkjk@16.com'
# content1 = re.findall(r'\w+@\w+.com', s4)
# print(content1)
#
# # 把以上合法的电子邮件地址替换成我自己的电子邮件地址
# content2 = re.sub(r'\w+@\w+.com','xiaofang@PythonOpen.com', s4)
# print(content2)

# 使用正则提取字符串中的单词
s5 = "i love you not because who 233 of 890sdxxx not"
content1 = re.findall(r'\b[a-zA-Z]+\b', s5)
# \b匹配字母或数字边界，\B 匹配非字母和数字边界
content2 = re.findall(r'[a-zA-Z]+\b', s5)
# search表示只匹配第一个值就返回
content3 = re.search(r'[a-zA-Z]+\b', s5)
# match表示从头开始匹配，content4和content5等价
content4 = re.match(r'[a-zA-Z]+\b', s5)
content5 = re.search(r'^([a-zA-Z]+\b)', s5)
print(content1)
print(content2)
print(content3.group())
print(content4.group())
print(content5.group())
