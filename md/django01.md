# Django系统
- 环境
    - python3.6
    - django1.8
- 参考资料
    - [django中文教程](http://python.usyiyi.cn/)
    - django架站的16堂课
# 环境搭建
- anoconda+pycharm
- anaconda使用
    - conda list:显示当前环境安装的包
    - conda env list:显示安装的虚拟环境列表
    - conda create -n env_name python=3.6
    - 激活conda的虚拟环境
        - (Linux)source activate env_name
        - (win) activate env_name
    - pip install django=1.8

# 后台需要的流程

# 创建第一个django程序
- 命令行启动
    - django-admin startproject tulingxueyuan
    - cd tulingxueyuan
    - python manage.py runserver
    
- pycharm启动
    - 需要配置

# 路由系统-urls
- 创建app
    - app:负责一个具体业务或者一类具体业务的模块
    - python manage.py starteapp teacher
    
- 路由
    - 按照具体的请求url，导入相应的业务处理模块的一个功能
    - django的信息控制中枢
    - 本质上是接受的URL和相应的处理模块的一个映射
    - 在接受URL请求的匹配上使用RE
    - URL的具体格式如urls.py中所示
- 需要关注两点：
    1. 接受的URL是什么，即如何用RE对传入URL进行匹配
    2. 已知URL匹配到哪个处理模块
- url匹配规则
    - 从上往下一个一个对比
    - url格式是分级格式，则按照级别一级一级往下对比，主要对应url包含子url的情况
    - 子url一旦被调用，则不会返回到主url
        - '/one/two/three'
    - 正则以r开头，表示不需要转义，注意尖号(^)和美元符号($)
        - '/one/two/three'配对r'^one/'
        - 'oo/one/two/three'不配对r'^one/'
        - '/one/two/three'配对r'^one/$'，以three结尾
        - 'oo/one/two/three'不配对r'^one/$'
        - 开头不需要有反斜杠
    - 如果从上向下都没有找到合适的匹配内容，则报错
# 正常映射
- 把某一个符合RE的URL映射到事务处理函数中去
    - 举例如下：
        、、、
        from showest import ciews as sv
        
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^normalmap/', do_admin02),
        ]
        、、、
# 3. URL中带参数映射
- 在事件处理代码中需要由URL传入参数，形如 /myurl/param中的param
- 参数都是字符串形式，如果需要整数等形式需要自行转换
- 通常的形式如下
    、、、
        /search.page/432中的432需要经常性变换，所以设置成参数比较合适
    、、、
# 4.URL在app中的处理
    - 如果所有应用URL都集中tulingxueyuan/urls.py中，可能导致文件的臃肿
    - 可以把urls具体功能逐渐分散到每个app中
        - 从django.conf.urls导入include
        - 注意此时RE部分的写法
        - 添加include导入
- 使用方法
    - 确保include被导入
    - 写主路由的开头url
    - 写子路由
    - 编写views函数        
- 同样可以使用参数
# 5.URL中的嵌套参数
    - 捕获某个参数的一部分
    - 例如URL /index/page-3,需要捕获数字作为参数
        、、、
        url(r'index_1/(page-(\d+)?$', sv.myindex_1), #不太好
        url(r'index_2/(?:page-(?P<page_number>\d+/)?$', sv.myindex_2), #好
        、、、
    - 上述例子会得到两个参数，但 ?：表明忽略此参数
        
# 6. 传递额外的参数
- 参数不仅仅来自于URL，还可能是我们自己定义的内容
    、、、
    url(r'extrem/$', sv.extremParam, {'name':'liudana'}),
    、、、
- 附加参数同样适用于include语句，此时对include内所有都添加

# 7.URL的反向解析
- 防止硬编码
- 本质上是对每一个URL进行命名
- 以后再编码代码中使用URL的值，原则上都应该使用反向解析

# views视图
# 1. 视图概述
- 视图即视图函数，接收web请求并返回响应的实物处理函数
- 响应指符合http协议要求的任何内容，包括json,string, html等
- 本章忽略事务处理，重点在如何返回处理结果上
# 2. 其他很简单视图
- django.http给我们提供类很多和HttpResponse类似的简单视图，
通过查看django.http代码我们知道，
- 总共django给我们定义了一下一些简单类
- 此类视图使用方法基本类似，可以通过return语句直接反馈返回给浏览器
- Http404为Exception子类，所以需要raise使用

# 3. HttpResponse详解
- 方法
    - init:使用页内容实例化HttpResponse对象
    - write(content):以文件的方式写
    - flush():以文件的方式输出缓存区
    - set_cookie(key, value="", max_age=None, expires=None):设置Cookie
        - key, value都是字符串类型
        - max_age是一个整数，表示在指定秒数后过期
        - expires是一个datetime或者timedelta对象，会话将在这个指定的日期/时间过期
        - max_age与expires二选一
        - 如果不指定过期时间，则默认两个星期后过期
    - delete_cookie(key):删除指定的key的Cookie,如果可以不存在则什么也不发生

# 4. HttpResponseRedirect
    - 重定向，服务器端一熬转
    - 构造函数的第一个参数用来指定重定向的地址
    - 案例 ShowViews/views.py
        、、、python
            # 在east/urls中添加一下内容
            url(r'^v10_1/', views.v10_1),
            url(r'^v10_2/', views.v10_2), 
            url(r'^v11/', views.v11, name="v11"),
        、、、
        、、、python
        # /east/ShowViews/views中添加一下内容
        def v10_1(request):
            return HttpResponseRedirect("/v11")
            
        def v10_1(request):
            return HttpResponseRedirect("v11")    
 
        def v11(request):
            return HttpResponse("哈哈，这是v11的访问返回呀？")
            
# 5. Request对象
- Request介绍
    - 服务器接收到http协议的请求后，会根据根报文创建HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 在django.http模块中定义了HttpRequest对象的API
- 属性
    - 下面除非特别说明，属性都是只读的
    - path:一个字符串，表示请求的页面的完整路径，不包含域名
    - method:一个字符串，表示请求使用的HTTP方法常用值包括：'GET'、'POST'
    - encoding:一个字符串，表示提交的数据的编码方式
        - 如果为None则表示使用浏览器的默认设置，一般为utf-8
        - 这个属性是可写的，可以通过修改它来修改访问表单数据使用编码，接下来对属性
    - GET：一个类似于字典的对象，包括get请求方式的所有参数
    - POST：一个类似于字典的对象，包括post请求方式的所有参数
    - FILES:一个类似于字典的对象，包含所有的上传文件
    - COOKIES：一个标准的Python字典，包含所有的cookie，键和值
    - session:一个既可读又可写的类似于字典的对象，表示当前的会话，
        - 只有当Django启用会话的支持才可用，详细内容见"状态保持"
- 方法：
    - is_ajax():如果请求是通过XMLHttpRequest发起的，则返回True
    - 
- QueryDict对象
    - 定义在django.http.QueryDict
    - request对象的属性GET、POST都是QueryDict类型的对象
    - 与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况
    - 方法get():根据键获取值
        - 只能获取键的一个值
        - 如果一个键同时拥有多个值，获取最后一个值
    - 方法getlist():根据键获取值
        - 将键的值以列表返回，可以获取一个键的多个值
- GET属性
    - QueryDict类型的对象
    - 包含get请求方式的所有参数
    - 与url请求地址中的参数对应，位于?后面
    - 参数的格式是键值对，如key1=value1
    - 多个参数之间，使用&链接，如key1=value1&key2=value2
    - 键是开发人员定下来的，值是可变的
    - 案例v8_get
    
- POST属性
    - QueryDict类型的对象
    - 包含post请求方式的所有参数
    - 与form表单中的控件对应
    - 表单中控件必须有name属性， name为键， value为值
        - checkbox存在一键多值的问题
    - 键是开发人员定下来的，值是可变的
    - 案例v9_post
- 手动编写视图
    - 实验目的：
        - 利用django快捷函数手动编写视图处理函数
        - 编写过程中理解视图运行原理
        
- 分析：
    - django把所有请求信息封装入request
    - django通过urls模块把相应请求跟事件处理函数连接起来，并把request作为参数传入
    - 在相应的处理函数中，我们需要完成两部分
        - 处理业务
        - 把结果封装并返回，我们可以使用简单HttpResponse，同样也可以用渲染结果
    - 本案例不介绍业务处理，把目光集中在如何渲染结果并返回
- render(request, template_name[, context][, context_instance][, content_type])
    - 使用模版和一个给定的上下文环境，返回一个渲染和HttpResponse对象
    - request:django的传入请求
    - template_name:模版名称
    - content:上下文环境
    - 案例teacher_app/views/render_test
    
- render_to_response
    - 根据给定的上下文字典渲染给定模版，返回渲染后的HttpResponse
    
- 系统内建视图
    - 系统内建视图
    - 404
        - default.page_not_found(request, template_name='404.html')
        - 系统引发Http404时发出
        - 默认错误request_path变量给模版，即导致错误的URL
        - DEBUG=True则不会调用404， 取而代之是调试信息
        - 404视图会被传递一个RequestContext对象并且可以访问模版上下文处理器提供的变量
        
        - 500(server error)
            - default.server_error(request, template_name='500.html')
            - 需要DEBUG=False，否则不调用
        - 403(HTTP Forbidden) 视图
            - default.permission_denied(request, template_name='403.html')
            - 需要PermissionDenied 触发
        - 400(bad request) 视图
            - default.bad_request(request, template_name='400.html')
            - DEBUG=False
            
# 8. 基于类的视图
- 和基于函数的视图的优势和区别
    - HTTP方法的method可以有各自的方法，不需要使用调教分支来解决
    - 可以使用OOP技术(例如Mixin)
- 概述
    - 核心是允许使用不同的实例方法来响应不同的HTTP请求方法，而避开条件分支实现
    - as_view函数作为类的可调用入库，该方法创建一个实例并调用dispatch方法，按照请求方法
    方法没有定义，则引发HttpResponseNotAllowed
- 类属性使用
    - 在类定义时直接覆盖
    - 在调用as_view的时候直接作为参数使用，例如：
    、、、
        urlpatterns = [
            url(r'^about/', GreetingView.as_view(greeting="G'day")),    
            ]
    、、、
- 对基于类的视图的扩充大致有三种方法：Mixin, 装饰as_view, 装饰dispatch
- 使用Mixin
    - 多继承的一种形式，来自父类的行为和属性组合在一起
    - 解决多继承的问题
    - View的子类只能单继承，多继承会导致不可期问题
    - 多继承带来的问题
        - 结构复杂
        、、、
        
# Models模型
- ORM
    - ObjectRelationMap:把面向对象思想转换成关系数据库
    - 类对应表格
    - 类中的属性对应表中的字段
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类型都必须使用model.xxx不能使用python中的类型
    - 在django中，Model负责跟数据库交互
- django链接数据库
    - 自带默认数据库sqllite3
        - 关系型数据库
        - 轻量级
    - 建议开发用自带默认数据库sqllite3,部属用mysql之类数据库
    - 
    # django连接mysql
    - 切换数据库在settings中进行设置
    、、、
    DATABASES = [
        'default' = {
            'ENGINE' : 'django.db.backends.mysql',
            'NAME' : '数据库名',
            'PASSWORD' : '数据库密码',
            'HOST' : '127.0.0.1',
            'PORT' : '3306',
        }
    ]
    、、、
    - 需要在项目文件下__init__文件中导入pymysql包
        、、、
        # 在住项目的__init__文件中
        import pymysql
        pymysql.install_as_MySQLdb()
        、、、
        
# models类的使用
- 定义和数据库表映射的类
    - 在应用中的models.py文件中定义class
    - 所有需要使用ORM的class都必须是models.Model的子类
    - class中的所有属性对应表格中的字段
    - 字段的类都必须使用models.xxx 不能使用python中的类型
- 字段常用参数
1. max_length:规定数值的最大长度
2. blank:是否允许字段为空，默许不允许
3. null: 在DB中控制是否控制是否保存为null,默认为false
4. default:默认值
5. unique: 唯一
6. verbose_name: 假名

- 数据库的迁移
    1.在命令行中，生成数据迁移的语句(生成sql语句)
        、、、
        python3 manage.py makemigrations
        、、、
    2. 在命令行中，输入数据迁移的指令
        、、、
        python3 manage.py migrate
        、、、
        ps:如果迁移中出现没有变化或者报错，可以尝试强制迁移
        、、、
        # 强制迁移命令
        python3 manage.py makemigrations 应用名
        python3 manage.py migrate
        、、、
    3. 对于默认数据库，为了避免出现混乱，如果数据库中没有数据，每次迁移前可以把
    自带的sqlite3数据库删除
    
、、、
1.启动命令行：python3 manage.py shell
ps:注意点：对orm的操作分为静态函数和非静态函数两种。静态是指在内存中只一个
2.在命令行中导入对应的映射类
    from应用.models import类名
3. 使用objects属性操作数据库。objects是模型中实际和数据库进行交互的
4. 查询命令
    - 类名.objects.all()查询数据库表中的所有内容，返回的结果是一个Query
    - 类名.objects.filter(条件)
、、、

# 保存数据
5. save()
- 常见查找方法
1. 通过查找格式：属性名__(用下面的内容) =值
- gt: 大于
- gte: 大于等于
- lt: 小于
- lte: 小于等于
- range: 范围
- year: 年份
- isnull: 是否为空

2. 查找等于指定值的格式： 属性名 = 值
3. 模糊查找: 属性名 __(使用下面的内容) = 值

* exact : 精准等于
* iexact: 不区分大小写
* contains: 包含
* startwith: 以..开头
* endwith: 以..结尾

# 数据库表关系
- 多表联查：
利用多个表联合查找某一项或者多项信息
- 1.1 
    - 建立关系，在模型任意一边即可，使用OneToOne
    - add:
        - 添加没有关系的一边，直接实例化保存就可以了
    - 添加有关系的一边，使用create方法也可以使用save方法
    - query:
        - 有子表查母表：由子表的属性直接提取信息
        - 由母表查子表：使用双下划线
            >>> s = School.objects.get(manager__manager_name="dana")
            >>> s
            <School: nanjingtulingxueyuan>
    - change:
        - 单个修改使用save
        - 批量修改使用update
        - 无论对子表还是对母表的修改
    - delete: 直接使用delete还是删除
- 1：N
    - 一个表格的一个数据项/对象等，可以有很个另一个表格的数据项
    - 比如：一个学校可以有很多个老师，但一个老师只能在一个学校里上班
    - 使用上
        - 使用ForeignKey
        - 在多的那一边，比如上边的例子就是在Teacher的表格里进行定义
        
    - Add:
        - 跟一对一的方法类似，通过create和new来创建
        - create:把属性都填满，然后不再需要手动保存
        - new:可以属性或者参数为空，必须用save保存
    - Query:
        - 以学校和老师的例子为准
        - 如果知道老师，查学校，则通过增加的关系属性，直接使用
        - 例如：查找t1老师是哪个学校的
        - 反查-
            - 有学校，查这个学校的所有老师，则系统自动在老师模型名称的小写下直接加下划线set
                用来表示
- N:N
    - 表示任意一个表的数据可以拥有对方表格多项数据，反之亦然
    - 比如典型的例子就是老师和学生的关系
    - 使用上，在任意乙方，使用ManyToMany定义，只需要定义一边
    
    - Add:
    - 添加老师，则在student.teacher.add()

    - Query:
        - 跟一对多类似，使用set查询
        

    


    

    

    
    

