from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from .forms import signup_form


def home(request):
    return render(request, 'home.html')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        print(form)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(
                username=username,
                password=password
            )
            if user is not None:
                auth.login(request, user)
                return redirect(home)
        return redirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'account/login.html', {'form': form})


def logout_view(request):
    auth.logout(request)
    return redirect(home)


def signup_view(request):
    if request.method == "GET":
        return render(request, 'account/signup.html')
    if request.method == "POST":
        form = signup_form(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect(home)
        return redirect("/signup")
    else:
        form = signup_form()
        return render(request, 'account/signup.html', {'form': form})
# 오류메세지 띄우기해야함
