from django.shortcuts import render

# Create your views here.
def about(response):
    return render(request,"about.html")

def contact(response):
    return render(request,"contact.html")