
from django.urls import path
from . import views


urlpatterns = [
   path('',views.home,name='homepage'),
   path("contact", views.contact, name="contact"),
]

