from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.create_Album,name='add_album'),
]
