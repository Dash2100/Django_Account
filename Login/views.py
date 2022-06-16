from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth
from django.http import HttpResponseRedirect as redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# def users(request):
#     a = User.objects.all()
#     return render(request, 'index.html', locals())

def index(request):
    return render(request, 'index.html', locals())

def login(request):
    #已登入導向至index
    if request.user.is_authenticated:
        return redirect('/index/')
    return render(request, 'login.html', locals())

def postlogin(request):
    if request.user.is_authenticated:
        return redirect('/index/')
    #接收POST並驗證
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    #確認使用者帳號存在,且已啟用
    if user is not None and user.is_active:
        auth.login(request, user)
        print(user)
        return redirect('/index/')
    else:
        return render(request, 'loginpost.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('/index/')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())