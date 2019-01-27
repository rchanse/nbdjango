from __future__ import unicode_literals
from django.http import Http404
#from django.template import loader             # tut 14
from django.shortcuts import render            #tut 14 short cut
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):          # tut 16 Http404
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does NOT exist")
    return render(request, 'music/detail.html', {'album': album})
#    return HttpResponse("<h2>Details for album_id:  " + str(album_id) + " </h2>")

