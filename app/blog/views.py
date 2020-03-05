from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm, UserForm, PostForm

from .auth import custom_authenticate

def login(request):
    if request.method == 'POST':
        user = custom_authenticate(request)
        if user is not None:
            print('yes authen!')
            return render(request, "base_post.html", {'user':user})
            # return HttpResponseRedirect(reverse('base_post'), context)
        else:
            return HttpResponse("Login Failed. Try again.")

    elif request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form':form})

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'base_post.html', {})
    else:
        form = UserForm()
        return render(request, 'register.html', {'form':form})

def base_post(request):
    if request.method == 'GET':
        print('request user : ', request.user)
        return render(request, 'base_post.html', {})

    # elif request.method == 'POST':
    #     form = PostForm(request.POST)
    #
    #     if form.is_valid():
    #         posting = form.save(commit=False)
    #         posting.user_id=
    #         form.save()