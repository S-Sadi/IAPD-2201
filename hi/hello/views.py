from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'User log in success')
            return render(request, 'home_page.html')
        else:
            messages.warning(request, 'User Not Found, Please register your account')
            return render(request, 'reg_istration.html')

    return render(request, 'log_In.html')


def registration(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.warning(request, 'This User already exist')
                return redirect('/registration')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email,
                                                username=username, password=password1).save()
                messages.success(request, 'Welcome')
                return redirect('login')

    return render(request, 'reg_istration.html')


def home(request):
    return render(request, 'home_page.html')


def logout(request):
    auth.logout(request)
    return render(request, 'log_In.html')


def index(request):
    product = Product.objects.all()
    # print(product)

    # context = {
    #     'pro' : product
    # }
    return render(request, 'index.html', locals())
