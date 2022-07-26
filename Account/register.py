from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'alert.html', {'type': 'success','title':'註冊成功','href':'/login/'})
    elif request.user.is_authenticated:
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})