from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posting/', views.posting, name='posting'),
    #path('posting/modify/', views.posting_modify, name='posting_modifiy'),
]