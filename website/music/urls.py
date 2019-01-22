# info for music app urls   (don't put in 
# ~/nbdjango/website/website/urls     collect under music

from django.conf.urls import url
from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
#    url(r'^admin/$  ', admin.site.urls),
    # /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detai'),
]
