from tarfile import REGULAR_TYPES
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from Login.views import *
from Register.views import *

urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
]
