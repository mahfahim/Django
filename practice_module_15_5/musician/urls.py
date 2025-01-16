from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.create_Musician,name='add_musician'),
]
