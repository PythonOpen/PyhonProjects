# Django REST Framework
# 1. REST
- 前后端分离
- API-ApplicationProgrammingInterface
    - 为了应付千变万化的前端需求
- REST:RepresatationsStateTrans
    - 20000 Fieding博士提出
    - RESTFUL:遵守REST规范的技术
- REST规范
    - URL代表一个资源,一个资源应该是一个名词
    - 动作有HTTP的methode方法提供
    - URL应该包含版本信息，版本信息也可以添加咋爱HTTP协议里面
    - 过滤信息，使用URL的参数代表过滤
    - 返回值：每一个返回码都有具体特定含义
    - 返回格式：推荐固定具体格式
    
- DjangoRestFramework
    - https://qlmi.github.io/Django-REST-framwork-documentation/
    - 安装：pip install djangorestframwork
    - 版本问题：version3.7是基于1.xx版本django,之后的2.xx版本django
    - django_filter依赖djangorestframework 3.7
- DRF的主要任务
- 案例TlxyDRF
    - django-admin startproject TlxyDRF
    - python manage.py startapp case01
    - 配置settings
    - 配置urls
    - 创建3个模型，Classroom, Teacher, Student
    - 创建序列化器
    - 创建视图集合
    
# 序列化
- pickle, file, xml,json
- stu = Student
    stu.name
    stu.age
- 序列化:把系统运行中的一些实例等转换成一种可直接表示出来的格式，用来保存，传输等
- 反序列化:序列化操作
# 序列化/反序列化-DRF
- 创建project DRF02
- 创建app MySer
- settings
# serializer的类型的参数
- read_only:仅用于序列化输出
- writer_only:仅用于反序列化输入
- required:反序列化时必须输入，默认是True
- allow_null:允许传入None
- validators:使用验证器
# 创建serializer对象/使用
- 构造方法
    Serializer(instance=None, data=empty, **kwarg)
    
- 反序列化
    - 验证
        - is_valid:
            - 数据是否合法，返回boolean
            - 在使用从外部传入的数据之前，必须使用此函数进行验证
            - 如果验证失败，返回数据错误异常
        - validate_data:
            - 经过验证后的数据，存入此结构
            
- 视图
    - DRF的视图的视图从处理任务，处理流程等跟Django基本一致
    - 此视图基本是django的扩展
    - Request
        - 把请求解析成一个request实例
        - 属于DRF的，跟django的HttpRequest不太一样
        - 在得到Request之前有一个Parse对传入的数据请求进行解析
        - data属性
            - 请求数据体，类似于Django的request.POST, request.FILES
            - 在DRF中主要指的是Json
        - query_params
            - 所有传入的关键字
                api.tulingxueyuan.com/student/?name='liu'
                # 使用案例
                name = self.request.query_param.get('name', None)
                
        - user
            - 登录后的用户信息都在user中
            - 如果没有登录，则是anoymous
            - 可以用来判断用户是否登录成功
        - Response
            - rest_framework.response.Response
            - 用Renderer渲染器对返回内容进行渲染
            
        - 返回的构造方式
            - return Response(, status=None, template_name=None, headers=None, content_type=None)
            - data:返回的数据
            - status:返回的状态码
                - 1xx:信息告知
                - 2xx:成功
                - 3xx:重定向
                - 4xx:请求错误
                - 5xx:服务器错误
- 视图类
- APIView
    - rest_framework.views.APIView
    - 是django中View的子类
    - 跟View有不同的地方
        - 传入传出数据用的是drf的请求和反馈类
        - 会引发并处理APIException
        - 在dispatch之前，会进行身份验证，权限检查，流量控制
    - 支持的属性有
        - authentication_classes:列表或者元组，身份验证类
        - permission_classes:进行权限验证
        - throttle_classes:流量控制类
        
    - 对API的访问提供了一些方便
        - HTTP-Method + 名词
        - 默认对HttpMethod的常用方法提供了支持
    - 案例：views-StudentAPIView
    
- API调试工具
    - chrome - postman
    - firefox - RESTClient
    
    - GenericAPIView
        - APIView的子类
        - 支持的属性
            - queryset:查询结果集
            - serializer_class:视图使用的序列化器类
            - panination_class:分页控制器
            - filter_backends:过滤器
            - lookup_field:查询条件字段，默认为pk
        - get_queryset:返回查询结果集集合，经常需要重写
        - get_serializer_class:得到序列化器类
        - get_serializer:得到序列化器
- ListModelMixin
    - list(request, *args, **kwargs)
- CreateModelMixin
    - create(request, *args, **kwargs)
- RetrieveModelMixin
    - retrieve(............)
- UpdateModelMixin
    - update(..........)
- DestroyModelMixin
    - destroy(..........)

- ViewSet
    - 把一系列操作打包放入一个类中
    - list：GET
    - retrieve:GET + id
    - destroy:DELETE
    - update:UPDATE
    - create:POST

        
        
            

          

    

