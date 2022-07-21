from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.contrib import auth

def login(request):
    #偵測是否為POST到此頁面
    if request.method == 'POST':
        #已登入用戶導向至首頁
        if request.user.is_authenticated:
            return redirect('/')
        #接收POST並驗證
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        #確認使用者帳號存在,且已啟用
        if user is not None and user.is_active:
            auth.login(request, user)
            print(user,"Logged in")
            return redirect('/')
        else:
            return render(request, 'alert.html', {'type': 'error','title':'錯誤','text':'帳號或密碼輸入錯誤','href':'/login/'})
    else:
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return redirect('/')