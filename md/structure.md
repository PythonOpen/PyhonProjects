# 结构化文件存储
- xml,json
- xml
- json

- xml(extensibleMarkupLuanguage) 可扩展标记语言
    - 标记语言：语言中使用尖括号括起来的文本字符串标记
    - 可扩展：用户可以自己定义需要的标记
    - 例如：
        <head>
            ......
        </head>
    - 是w3c组织制定的一个标准
    - xml描述的是数据本身，即数据结构和语义
    - HTML侧重于如何显示web页面中的数据
    
- XML文档的构成
    - 处理指令（可以认为一个文件内只有一个处理指令）
    - 根元素（一个文件内只有一个根元素）
        - 可看成一个树形结构
    - 属性
    - 内容
        - 表明标签所储存的信息
    - 注释
    
# xml访问

# 读取
- xml读取分两个主要技术，SAX,DOM
- SAX(Simple API for XML)
    - 基于时间驱动的API
    - 利用SAX解析文档设计到解析器和事件处理两部分
    - 特点：
        - 块
        - 流式读取
- DOM
    - 是W3C规定的xml编程接口
    - 一个xml文件再缓存中以何种结构保存，读取
    - minidom
    
    - etree
    
- xml文件的写入
    - 更改
        - ele.set:修改属性
        - ele.append:添加子元素
        - ele.remove
    - 生成创建
        - SubElement
        - minidom生成
        - etree创建
    