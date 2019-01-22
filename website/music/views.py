from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Album


def index(request):
    all_albums = Album.objects.all()     # connect to DB get data
    html = ''
    for album in all_albums:             # access albums one-by-one
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'   
    return HttpResponse(html)
#   return HttpResponse("<h1>This will be a list of all albumsb</h1>")

def detail(request,album_id):
    return HttpResponse("<h2>Details for album_id:  " + str(album_id) + " </h2>")

