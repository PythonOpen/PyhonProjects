# 页面解析和数据提取
- 结构数据： 现有的结构，在谈数据
    - JSON文件
        - JSON Path
        - 转换成Python类型进行操作(json类)
    - XML文件
        - 转换成python类型（xmltodict)
        - XPath
        - CSS选择器
        - 正则
- 非结构化数据：先有数据，再谈结构
    - 文本
    - 电话号码
    - 邮箱地址
        - 通常处理此类数据，使用正则表达式
    - Html文件
        - 正则
        - XPath
        - CSS选择器
# 正则表达式
- 一套规则，可以在字符串文本中进行搜查替换等
- 案例25 re的基本使用流程
- 案例25 match的基本使用
    - match:从开始位置开始查找，一次匹配
    - search:从任何位置查找，一次匹配
    - findall: 全部匹配，返回列表
    - finditer:全部匹配，返回迭代器
    - split: 分割字符串，返回列表
    - sub: 替换
- 匹配中文
    - 中文unicode范围主要在[u4e00-u9fa5] 案例28
    
- 贪婪，非贪婪模式
    - 贪婪模式：尽可能多的匹配
    - 非贪婪模式：尽可能少的匹配
    - python里，默认为贪婪模式
        - 例子：正则：ab* abbbbbbcccccc
        - 贪婪模式：abbbbbb
        - 非贪婪模式：a

# XML

# XPath
- XPath(XML Path Language), 是一门在XML文档中查找信息的语言
- XPath开发工具
    - 开源的XPath表达式工具：XMLQuire
    - chrome插件：XPath Helper
    - Firfox插件：XPath CHecker
    
- 常用路径表达式
    - nodename:选取此节点的所有子节点
    - /:从根节点开始找
    - //：选取元素，而不考虑元素的具体位置
    - .：当前节点
    - ..: 父节点
    - @: 选取属性
    - 案例：
        - school:选取school下所有子节点
        - /school：选取根元素
        - school/student:选取school的所有为student的子元素
        - //student:选取studen元素
        - //@lang:选取名称为lang的所有属性
        
    - 谓语(Predicates)
        - 谓语用来查找某个特定的节点，被写在方括号中
        - /school/student[1]:选取第一个属于school下的student元素
        - /school/student[last()]:选取最后一个属于school下的student元素
        - /school/student[last()]:选取倒数第二个属于school下的student元素
        - /school/student[position()<3]:选取属于school下的前两个student元素
        - /school/student[@lang]
        - /school/student[@lang="cn"] 
        - /school/student[@price<90]
        - /school/student[@price<90]/name
        
    - 通配符
        - *：任何元素节点
        - @*：匹配任何属性节点
        - node():匹配任何类型的节点
    - 选取多个路径
        - //school | //student/name
      
# lxml库
- python的HTML/XML的解析器
- 功能
    - 解析HTML,案例29
    - 文件读取，案例30
    - etree和XPath的配合使用，案例31
# CSS选择器 BeatifulSoup4
 - 几个常用爬取信息工具的比较：
    - 正则：很快，不好用，不需安装
    - baautifulsoup: 慢，使用简单，安装简单
    - lxml:比较快，使用简单，安装一般
    - 案例32
- 四大对象
    - Tag
    - NavigableString
    - BeatytifulSoup
    - Comment
- Tag
    - 对应Html中的标签
    - 可以通过soup.tag_name
    - tag两个重要属性
        - name
        - attrs
    - 案例33  
- NavigableString
    - 对应内容值   
- BeatytifulSoup
    - 表示的是一个文档的内容，大部分可以把他当作tag对象
    - 一般我们可以用soup来表示 
- Comment
    - 特殊类型的NavigableString对象
    - 对其输出，则内容不包括注释符号
    
- 遍历文本对象
    - contents: tag的子节点以列表的方式给出
    - childrens: 子节点以迭代器形式返回
    - descendants: 所有子孙节点
    - string: 内容
    - 案例34
    
- 搜索文档对象
    - find_all(name, attrs, recursive, text, ** kwargs)
        - name:按照那个字符串搜索，可以传入的内容为
            - 字符串
            - 正则表达式
            - 列表
        - keyword参数，可以用来表示属性
        - text:对应tag文本值
        - 案例35
        
- CSS选择器
    - 使用soup.select,返回一个列表
    - 通过标签名称： soup.select("title")
    - 通过类名： soup.select(".content")
    - id查找： soup.select("#name_id")
    - 组合查找： soup.select("div #input_content")
    - 属性查找： soup.select("img[class='photo']")
    - 获取tag内容： tag.get_text
    - 案例36
    
- re的使用步骤
1. compile函数正则表达式的字符串便以为一个Pattern对象
2. 通过Pattern对象的一些方法对文本进行匹配，匹配结果是一个Match对象
3. 用Match对象的方法，对结果进行操纵

# 动态HTML

## 爬虫跟反爬虫

# 动态HTML介绍
- JavaScript
- jQuery
- Ajax
- DHTML
- Python采集动态数据
    - 从Javascript代码入手采集
    - Python第三方库运行javaScript,直接采集你在浏览器看到的页面
    
## Selenium + PhantomJS
- Selenium: web自动化测试工具
    - 自动加载页面
    - 获取数据
    - 截屏
    - 安装：pip install selenium==2.48.0
    - 官网：http://selenium-python.readthedocs.io/index.html
- PhantomJS(幽灵)
    - 基于Webkit 的无界面的浏览器
- Selenium 库有一个WebDriverde的API
- WebDriver可以跟页面上的元素进行各种交互，用它可以进行爬取
- 案例39

- chrome + chromedriver
- Selenium操作主要分两大类：
    - 得到UI元素
        - find_element_by_id
        - find_elements_by_name
        - find_elements_by xpath
        - find_elements_by_link_text
        - find_elements_by_partial_link_text
        - find_elements_by_tag_name
        - find_elements_by_class_name
        - find_elements_by_css_selector
    - 基于UI元素操作的模拟
        - 单击
        - 右键
        - 拖拽
        - 输入
        - 可以通过导入ActionsChains类来做到
    - 案例40
    
# 验证码问题
- 验证码：防止机器人或者爬虫
- 分类：
    - 通用方法：
        - 下载网页和验证码
        - 手动输入验证码
    - 简单图片
        - 使用图像识别软件或者文字识别软件
        - 可以使用第三方图像验证破解网站，如www.chaojiying.com 
    - 极验
        - 破解比较麻烦
        - 可以模拟鼠标等移动
        - 一直在进化
    - 12306
    - 电话：语音识别
    - google验证
    
# Tesseract
- 机器视觉领域的基础软件
- OCR:OpticalChracterRecognition,光学文字识别
- Tesseract: 一个ocr库，有google赞助
- 安装：
    - windows:https://jingyuan.baidu.com/aeticle/219f4bf788addfde442d38fe.html
- 安装完后还需要pytesseract
    - pip install pytesseract
- 读取案例：案例41
    
