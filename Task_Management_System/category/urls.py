from django.urls import path
from . import views
urlpatterns = [
    path("add/",views.Add_category,name="add_category"),
]
