from django.shortcuts import render, get_object_or_404, redirect
from . import forms
from . import models


def create_musician(request):
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MusicianForm()
    return render(request, 'musician_form.html', {'form': form})


def edit_musician(request, id):
    musician = get_object_or_404(models.Musician, pk=id)
    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = forms.MusicianForm(instance=musician)
    return render(request, 'musician_form.html', {'form': form})


def delete_musician(request, id):
    musician = get_object_or_404(models.Musician, pk=id)
    musician.delete()
    return redirect('home')
