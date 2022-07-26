from tarfile import REGULAR_TYPES
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Account.login import *
from Account.register import *
from Account.password import *

def index(request):
    return render(request, 'home.html', {'IsHome': "active"})

@login_required(login_url='/login/')
def second(request):
    return render(request, 'second.html', {'IsSecond': "active"})

# @login_required(login_url='/login/')
# def password(request):
#      return render(request, 'password.html')

urlpatterns = [
    path('', index),
    path('second/', second),
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('password/', change_password),
]
