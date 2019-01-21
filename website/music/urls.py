# info for music app urls   (don't put in 
# ~/nbdjango/website/website/urls     collect under music

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
#    url(r'^admin/$  ', admin.site.urls),
]
