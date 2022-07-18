from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect as redirect
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    discord = forms.CharField(
        label="Discord ID:",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','discord')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/login/')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        form = RegisterForm()
    return render(request, 'register.html', locals())