from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('practice_app.urls')),  # Change 'practice_app' to your app's name
]
