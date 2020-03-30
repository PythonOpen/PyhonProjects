from django.conf.urls import include, url
from django.contrib import admin
from teacher_app import views as v

urlpatterns = [
    # Examples:
    # url(r'^$', 'tulingxueyuan_views.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^teacher/', v.teacher),
    url(r'^v2_exp/', v.v2_exception),

    url(r'^v10_1/', v.v10_1),
    url(r'^v10_2/', v.v10_2),
    url(r'^v11/', v.v11, name="v11"),

    url(r'^v8/', v.v8_get),

    url(r'^v9_get/', v.v9_get),
    url(r'^v9_post/', v.v9_post),

    url(r'^render01_test/', v.render01_test),
    url(r'^render02_test/', v.render02_test),
    url(r'^render03_test/', v.render03_test),
    url(r'^render04_test/', v.render04_test),

    url(r'^get404/', v.get404),
]
