from django.shortcuts import render, redirect
from . import forms

# Create your views here.

def Add_category(request):
    if request.method == 'POST':
        Category_form = forms.CategoryForm(request.POST)
        if Category_form.is_valid():
            Category_form.save()
            return redirect('add_category')
    else:
        Category_form = forms.CategoryForm
    return render(request, "add_category.html", {"form": Category_form})
