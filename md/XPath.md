# XPath
- 在XML文件中查找信息的一套规则/语言，根据XML的元素或者属性进行遍历
- http://www.w3school.com.cn/xpath/index.asp
# XPath开发工具
- 开源的XPath表达式编辑工具：XMLQuire
- Chrome插件：XPath Helper
- Firedox插件：XPath Checker

# 选取节点
- nodename:选取此节点的所有子节点
- /:从根节点开始选取
- //：选取节点，不考虑位置
    - //age:选取出三个节点，一般组成列表返回

- .:选取当前节点
- ..:选取当前节点的父亲节点
- @：选取属性
- xpath中查找一般按照路径方法查找
    School/Student：返回Student节点（3个节点）
    //Student:选取所有Student的节点，不考虑位置
    School//Age:选取School后代中的所有Age节点
    //@desc：选取desc属性
    //Student[@desc]:选取带有属性desc的Age
    
# 谓语- Predicates
- /School/Student[1]:选取School下面的第一个Student节点
- /School/Student[last()]
- /School/Student[last()-1]
- /School/Student[position()<3] 
- //Student[@score]
- //Student[@score="99"]
- //Student[@score]/Age:选取带有属性score的Student节点的子节点Age

# xpath的一些操作
- |：或者
    //Student[@score] | //name:选取带有属性score的Student节点或者name节点
- 其余不常见的xpath运算符包括+,-,*，div,>,<