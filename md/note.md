- 添加搜索路径
    sys.path.append(dir)
    
# 包
- 包是一种组织管理代码的方式，包里面存放的是模块
- 用于将模块包含在一起的文件
- 自定义包的结构

# 调试技术
- 调试流程：单元测试->集成测试->交测试部
- 分类：
    - 静态调试：
    - 动态测试：
# pdb调试
- pdb:python调试库

# pycharm调试
- run/debug模式
- 断电：程序的某一行，程序在debug模式下
- 单元测试
# LOG
- 日志
- 日志的级别(level)
    - 不同的用户关注不同的程序信息
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO操作=>不要频繁操作
- LOG的作用
    - 调试
    - 了解程序的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# Logging模块
- 日志级别
    - 级别可自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别，只有当级别等于或者高于指定级别才被记录
- 使用方式
    - 直接使用logging(封装了其他组件)
    - Loging四大组件直接定制
    - logging.debug(msg,*args,**kwargs)创建一条严重级别的DEBUG日志记录
    - logging.info(msg,*args,**kwargs)创建一条严重级别的INFO日志记录
    - logging.warning(msg,*args,**kwargs)创建一条严重级别的WARNING日志记录
    - logging.error(msg,*args,**kwargs)创建一条严重级别的ERROR日志记录
    - logging.critical(msg,*args,**kwargs)创建一条严重级别的CRITICAL日志记录
    - logging.log(,*args,**kwargs)创建一条严重级别的level日志记录
    - logging.basicConfig(*kwargs）对root logger进行一次性配置
- logging.basicConfig(*kwargs）对root logger进行一次性配置 
    - 只是在第一次调用的时候起作用
    - 不配置logger则使用默认值
        - 输出：sys.stderr
        - 级别：WARNING
        - 格式：lever:log_name:content
        
# 2.1 logging模块的处理流程
    - 四大组建
        - 日志器(Logger):产生日志的一个接口
        - 处理器(Handler):把产生的日志发送到相应的目的地
        - 过滤器(Filter):更精细的控制那些日志输出
        - 格式器(Formatter):对输出信息进行格式化
        
    - Logger
        - 产生一个日志
        - 操作
            - logger.setLevel()设置日志器将会处理日志消息的最低严重级别
            - logger.addHandler()和logger.removeHandler()为该logger对象添加和移除一个处理器
            - logger.addFilter()和logger.removeFilter()为该logger对象添加和移除一个filter
            - logger.debug()：产生一条debug级别的日志，同理，info,error.等
                - logger.exception():创建类似于logger.error的日志消息
                - logger.log():获取一个明确的日志level参数类创建一个日志记录
        - 如何得到一个logger对象
            - 实例化
            - logging.getlogger()
    - Handeler
        - 把log发送到指定位置
        - 方法
            - setLevel
            - setFormat
            - addFilter,removeFilter
        - 不需要直接使用，Handler是基类
            - logging.StreamHandler 将日志信息发送到输出到Stream
            - ......
            
    - Format
        - 直接实例化
        - 可以继承Format添加特殊内容
        - 三个参数
            - fmt:指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
            - datafmt:指定日期格式字符串，如果不指定该参数则默认使用”%Y-%m-%d %H:%M:%S"
            - style:Python 3.2新增的参数。可取值为‘%’，‘{’和‘$’,如果不指定该参数则默认使用‘%’
       
    - Filter
        - 可以被Handler和Logger使用
        - 控制传递过来的信息的具体内容
      
    