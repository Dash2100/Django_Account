from tarfile import REGULAR_TYPES
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Login.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('postlogin/', postlogin),
]
