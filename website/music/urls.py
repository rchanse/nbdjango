# tut 21 add namespace  app_name
# info for music app urls   (don't put in 
# ~/nbdjango/website/website/urls     collect under music

from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),
#    url(r'^admin/$  ', admin.site.urls),
    # /music/712/   /music/album_id/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]
