from django.conf.urls import include, url
from django.contrib import admin
# 导入drf的路由
from rest_framework import routers
from MySer import views
# 定义一个DRF的简单路由
router = routers.DefaultRouter()
# router.register(r'student', views.StudentVS, base_name="stu")
router.register(r'student', views.StudentViewSet, base_name="stu")

urlpatterns = [
    # Examples:
    # url(r'^$', 'DFR02.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^api/', views.StudentAPIView.as_view()),
    # url(r'^apiView/', views.StudentGenAPIView.as_view()),
    url(r'^stuView/', include(router.urls)),
    # url(r'^api/', include(router.urls)),
]
