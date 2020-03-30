from django.conf.urls import include, url
from django.contrib import admin
# 导入路由
from rest_framework import routers
from case01 import views
router = routers.SimpleRouter()

router.register(r'student', views.StudentVS)

urlpatterns = [
    # Examples:
    # url(r'^$', 'TlxyDRF01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),

    url(r'^api/', include(router.urls)),
]
