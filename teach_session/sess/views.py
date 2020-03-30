from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView


# Create your views here.
'''
class StudentListView(ListView):

    需要设置两个主要内容
    1. queryset: 数据来源集合
    2. template_name:模版名称

    queryset = Student.objects.all().filter(gender="nan")
    template_name = "student_list.html"

    def as_view(self, request):
        return None




def mySess(request):
    print(type(request.session))
    print(request.session)
    # 如果session中没有teacher,则返回NoName
    print(request.session.get("teacher_name", "NoName"))

    # 清楚session所有的值
    request.session.clear()

    print("In mySess")
    return None


def student(request):

    请求所有学生的详情列表
    :param request:
    :return:

    # 大约有10000个学生
    stus = Student.objects.all()
    # 两个参数
    # 1.数据来源，也即从数据路中查询出的结果
    # 2. 单页返回的数据量
    p = Paginator(stus, 40)
    # 对Paginator进行设置或者对变量属性使用
    print(p.count)  # p里面有多少数据
    print(p.num_pages)   # 页面总数
    print(p.page_range)  # 页码列表，从1开始

    # 取得第三页的内容
    # 如果页码不存在， 报异常InvalidPage
    p.page(3)
    return stus
'''