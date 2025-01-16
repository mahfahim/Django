
from django.shortcuts import render,redirect
from . import forms 
from . import models


def create_Musician(request):
   if request.method == 'POST':
      musician_form = forms.MusicianForm(request.POST)
      if musician_form.is_valid():
         musician_form.save()
         return redirect('create_Musician')
      
   else:
      musician_form = forms.MusicianForm()
   return render(request,'musician.html',{'form':musician_form})

