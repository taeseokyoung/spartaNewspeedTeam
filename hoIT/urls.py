from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from account import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('home/', views.home, name='home'),
=======

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),
>>>>>>> feed
]
