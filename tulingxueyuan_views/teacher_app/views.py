from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import loader
from django.views import defaults
# Create your views here.


def teacher(r):
    return HttpResponse("这是teacher的一个视图")


def v2_exception(r):
    raise Http404
    return HttpResponse("OK")


def v10_1(request):
    return HttpResponseRedirect("/v11")


def v10_2(request):
    return HttpResponseRedirect(reverse("v11"))


def v11(request):
    return HttpResponse("哈哈，这是v11的访问返回呀？")


def v8_get(request):
    rst = ""
    for k,v in request.GET.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of Request is {0}".format(rst))


def v9_get(request):
    # 渲染模版并返回
    return render_to_response("for_post.html")


def v9_post(request):
    rst = ""
    for k,v in request.POST.items():
        rst += k + "-->" + v
        rst += ","
    return HttpResponse("Get value of Request is {0}".format(rst))


def render01_test(request):

    # 环境变量
    # c = dict()
    rsp = render(request, "render01.html")
    return rsp


def render02_test(request):

    # 环境变量
    c = dict()

    c["name01"] = "LiuDana"
    c["name02"] = "LiuErna"
    c["name03"] = "LiuSana"

    rsp = render(request, "render02.html", context=c)
    return rsp


def render03_test(request):

    # 得到模版
    t = loader.get_template("render02.html")
    print(type(t))

    r = t.render({"name01": "LiuDana"})
    print(type(r))

    return HttpResponse(r)


def render04_test(request):

    rsp = render_to_response("render02.html", context={"name01": "LiuDana"})
    return rsp


def get404(request):
    return defaults.page_not_found(request, template_name="render02.html")

