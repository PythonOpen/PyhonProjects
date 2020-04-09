"""
logging.debug
logging.info
logging.warning
logging.error
logging.critical
"""
# import logging
#
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# # level为logging的严重等级，该等级及以上的日记会显示记录，默认WARNING级别及以上会记录
# # logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
# # filename="my.log"为日志记录到该文件中
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="my.log")
#
# logging.debug("this is debug")
# logging.info("this is info")
# logging.warning("this is warming")
# logging.error("this is error")
# logging.critical("this is critical")

"""
# 装饰器
使用装饰器，打印函数的执行时间
"""
# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
#
#
# def log(func):
#     def wrapper(*arg, **kw):
#         logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT)
#         logging.info("this is info message")
#         return func(* arg, **kw)
#     return wrapper
#
#
# @ log
# def test():
#     print("test done")
#
#
# test()


"""
使用装饰器，根据不同的函数，传入的日志不相同
"""
# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="xxx.log")
#
#
# def log(text):
#     def decorator(func):
#         def wrapper(*arg, **kw):
#             logging.info(text)
#             return func(* arg, **kw)
#         return wrapper
#     return decorator
#
#
# @log("test done")
# def test():
#     print("test done")
#
#
# @log("main done")
# def main():
#     print("main done")
#
#
# test()
# main()


# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="xxx.log")
#
#
# def log(func):
#     def wrapper(*arg, **kw):
#         # 打印函数名
#         print(func.__name__)
#         logging.warning("this is warning message")
#         return func(*arg, **kw)
#     # return func 和return func()的区别:
#     # 使用return func 时返回的是func 这个函数；使用return func() 时返回的是func() 执行后的返回值，如果func()函数没有返回值则返回值为None
#     # return wrapper
#     return wrapper()
#
#
# # @log
# def test():
#     pass


# test()等价于log(test)
# log(test)
# test()

# import logging
# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(level=logging.DEBUG, format=LOG_FORMAT, filename="xxx.log")
#
#
# def log(text, func):
#     def decorator(func):
#         def wrapper(*arg, **kw):
#             logging.info(text)
#             return func(* arg, **kw)
#         # return wrapper
#         return wrapper()
#     # return decorator
#     return decorator(func)
#
#
# # @log("xixi")
# def test():
#     pass
#
#
# # test()等价于log("xixi", test)
# log("xixi", test)


"""
用logging的四大组件来实现日志的功能
打印出函数执行的时间，日志的等级，日志的消息
用装饰器
不同的日志，要记录不同等级的日志消息
"""
import logging
logger = logging.getLogger("mylogger")
logger.setLevel(logging.DEBUG)

# handler
# TimeRotationFileHandler是用来按照日期去划分日志
# RotationFileHandler是按照日志文件的大小划分日志
debug_handler = logging.FileHandler("408debug.log")
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

error_handler = logging.FileHandler("408error.log")
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(debug_handler)
logger.addHandler(error_handler)


def log(func):
    def wrapper(*arg, **kw):
        logger.debug("this is a debugger info")
        logger.error("this is a error info")
        return func(*arg, **kw)
    return wrapper


"""
根据函数的不同，要在日志中打印出不同的东西
"""


def log_higher(text):
    def decorator(func):
        def wrapper(*arg, **kw):
            logger.debug(text)
            logger.error(text)
            return func(*arg, **kw)
        return wrapper
    return decorator


@log
def test():
    print("test done")


@log_higher("this is test1 done")
def test1():
    print("test1 done")


@log_higher("this is main done")
def main():
    print("main done")


test()
test1()
main()

"""
一般情况我们在实际工作当中，
我们经常把logging封装成一个装饰器，
按照我们自己的习惯，例如新建一个loggerTools的文件
在需要保存日志的地方，把loggerTools引进引出。
"""
