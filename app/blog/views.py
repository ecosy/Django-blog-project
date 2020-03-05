from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        user_id = request.POST['user_id']
        password = request.POST['password']
        user = authenticate(request, user_id=user_id, password=password)
        print("user : ", user)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('base_post'))
        else:
            return HttpResponse("Login Failed. Try again.")

        # if login_form.is_valid():
        #     return HttpResponseRedirect(reverse('base_post'))

    elif request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            # new_user = User.objects.create_user(**form.cleaned_data)
            # login(request, new_user)
            form.save()
            return render(request, 'base_post.html', {})
            # return redirect('hello')
    else:
        form = UserForm()
        return render(request, 'register.html', {'form':form})

def base_post(request):
    if request.method == 'GET':
        return render(request, 'base_post.html', {})

    # elif request.method == 'POST':
