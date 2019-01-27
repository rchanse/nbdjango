# put in shortcut for Htpp404  replace try-except code by get_.. function
from django.shortcuts import render, get_object_or_404     
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    return render(request, 'music/index.html', {'all_albums': all_albums})


def detail(request, album_id):          # tut 16 Http404
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})
