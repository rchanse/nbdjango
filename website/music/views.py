from __future__ import unicode_literals
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This will be a list of all albumsb</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details for album_id:  " + str(album_id) + " </h2>")

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

