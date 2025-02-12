from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from . import models


def create_album(request):
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AlbumForm()
    return render(request, 'album_form.html', {'form': form})


def edit_album(request, id):
    album = get_object_or_404(models.Album, pk=id)
    if request.method == 'POST':
        form = forms.AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.AlbumForm(instance=album)
    return render(request, 'album_form.html', {'form': form})


def delete_album(request, id):
    album = get_object_or_404(models.Album, pk=id)
    album.delete()
    return redirect('home')
