from django.shortcuts import render
import datetime

def home(request):
    d = {'val1':[1,2,3,4],"val2":4,"slash":"I'm Fahim.", 
    "capital":"my name is fahim. i am from feni",
    "temp":"Fahim","NewYear": datetime.datetime(2025,1,20),
    "val_emp":"",
    "inner_dic": [
            {'name': 'zed', 'age': 19},
            {'name': 'amy', 'age': 22},
            {'name': 'joe', 'age': 31},
            ],
     "val10":21,
     "file":123456789,
     "lst":['a','b','c','d','e'],
     "line":["fahim",
     "Rahim",
     "Karim"],
     "val30":"MY NAME IS Fahim",
     "val31":"Fahim",
     "val32":"fahim is 23 .    I am",
     "past_date": datetime.datetime(2024, 12, 25, 15, 45, 0),
     
    }
    return render(request,'home.html',d)
