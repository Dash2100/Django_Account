from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib import auth
from .forms import ChangePasswordForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            auth.logout(request) # 登出使用者
            return render(request, 'alert.html', {'type': 'success','title':'密碼更改成功','href':'/login/'})
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'password.html', {'form': form})