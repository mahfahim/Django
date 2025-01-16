from django.shortcuts import render,redirect
from . import forms 
from . import models


def create_Album(request):
   if request.method == 'POST':
      album_form = forms.AlbumForm(request.POST)
      if album_form.is_valid():
         album_form.save()
         return redirect('album_form')
      
   else:
      album_form = forms.AlbumForm()
   return render(request,'home.html',{'form':album_form})


