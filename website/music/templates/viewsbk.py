# rch notes - similar to  music/views.py before tutor 16 Http404
from __future__ import unicode_literals
from django.http import Http404
from django.http import HttpResponse
#from django.template import loader             # tut 14
from django.shortcuts import render            #tut 14 short cut
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    context = {'all_albums': all_albums}
    return render(request, 'music/index.html', context)

# tutor 14
##def index(request):
##    all_albums = Album.objects.all()     # connect to DB get data3
##    template =  loader.get_template('music/index.html')
##    # pass var by a dict   std is call dix  context
##    context = {
##            'all_albums': all_albums,
##            }
##    return HttpResponse(template.render(context, request))
# end tutor 14

# material below was in prev tut 12
##def index(request):
##    all_albums = Album.objects.all()     # connect to DB get data
##    html = ''
##
##for album in all_albums:             # access albums one-by-one
##        url = '/music/' + str(album.id) + '/'
##        html += '<a href="' + url + '">' + album.album_title + '</a><br>'   
##    return HttpResponse(html)
###   return HttpResponse("<h1>This will be a list of all albumsb</h1>")

def detail(request, album_id):          # tut 16 Http404
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does NOT exist")

# pre tut 16
##def detail(request,album_id):
##    return HttpResponse("<h2>Details for album_id:  " + str(album_id) + " </h2>")
# end pre tut16
