from tarfile import REGULAR_TYPES
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Login.views import *
from Register.views import *

def index(request):
    return render(request, 'home.html', {'IsHome': "active"})

def second(request):
    if request.user.is_authenticated:
        return render(request, 'second.html', {'IsSecond': "active"})
    else:
        return HttpResponseRedirect('/login/')

urlpatterns = [
    path('', index),
    path('second/', second),
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]
