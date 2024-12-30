from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    return HttpResponse("This is first app courses page")

def about(request):
    return HttpResponse("This is first app about page")

def home(request):
    # return HttpResponse("This is first app home page")
    return render(request,'first_app/home.html')