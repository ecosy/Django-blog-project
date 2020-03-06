from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .models import Introduction
from django.views import View

from .forms import UserForm, IntroductionForm, LoginForm

class LoginView(View):
    def post(self, request):
        login_form = LoginForm(request.POST)
        user_id = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=user_id, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('base_post'))
        else:
            return HttpResponse("Login Failed. Try again.")

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form})


class RegisterView(View):
    def post(self, request):
        form_user = UserForm(request.POST)
        form_introduction = IntroductionForm(request.POST)

        if form_user.is_valid() and form_introduction.is_valid():
            last_name = form_user.cleaned_data['last_name']
            password = form_user.cleaned_data['password']
            user_id = form_user.cleaned_data['username']
            description = form_introduction.cleaned_data['description']

            # user model 저장
            user = User.objects.create_user(username=user_id, password=password, last_name=last_name)
            user.save()

            # introduction model 저장
            user_pk_id = User.objects.get(username=user_id).id
            intro = Introduction(description=description, user_pk_id=user_pk_id)
            intro.save()

            login(request, user)
            return HttpResponseRedirect(reverse('base_post'))

        else:
            return HttpResponse('error in RegisterView')

    def get(self, request):
        form_user = UserForm()
        form_intro = IntroductionForm()
        return render(request, 'register.html', {'form_user': form_user, 'form_intro': form_intro})

class BasePostView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, 'base_post.html', {'user': request.user})
        else:
            return HttpResponse('please login first.')

