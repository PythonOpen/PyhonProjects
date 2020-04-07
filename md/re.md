# 正则表达式（RegularExpression,re)
    - 是一个计算机科学的概念
    - 用于使用单个字符串来描述，匹配符合某个规则的字符串
    - 常常用来检索，替换某些模式的文本
# 正则的写法
- .(点号)：表示任意一个字符，除了\n,比如查找所有的一个字符\.
- []:匹配中括号中列举的任意字符，比如[L,Y,0],（LLY,Y0）true,LIU(false)
- \d:任意一个数字
- \D:除了数字都可以
- \s:标识空格，tab键
- \w:单词字符，就是a-z,A-Z,0-9,_
- \w:除了上面都行
- *:表示前面内容重复零次或者多次，\w*
- +:表示前面内容至少出现一次
- ?:前面才出现的内容零次或者一次
- (m,n):允许前面的内容出现至少m次，最多n次
- ^:匹配字符串的开始
- $:匹配字符串的结尾
- \b:匹配单词的边界
- ():对正则表达式内容进行分组，第一个括号开始，编号逐渐增大
    - 验证一个数字：^\d$
    - 必须有一个数字，最少一位:^\d+$
    - 只能出现数字，且位数为5-10位：^\d{4,10}$
- \A:只匹配字符串开头，\Aabcd...,则abcd...
- \Z:只匹配字符串开头，abcd\Z,则...abcd
- |:左右任意一个
- (?P<name>...):分组，除了原来的编号再制定一个别名
- (?P=name):引用分组
        