from __future__ import unicode_literals
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the RCH music homepage</h1>")


# -*- coding: utf-8 -*-
#
#from django.shortcuts import render
#from . import views
#
## Create your views here.
#
#urlpatterns = [
#        url(r'^$' , views.index, name='index'),
#        ]

