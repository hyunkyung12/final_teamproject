# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.models import User

from blog.models import *

'''
from .forms import LoginForm, RegisterForm

@ensure_csrf_cookie
def login_view(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/')
    
    return render(request, 'users/login.html', {'loginform': form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def register_view(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            email = form.cleaned_data
            user.email = email['email']
            user.save()

            return HttpResponseRedirect('/')

    return render(request, 'users/register.html', {'registerform': form})
'''

@login_required
def profile_view(request):
    context = {}
    if request.user.is_authenticated():
        user = User.objects.get(username=request.user)
        context = {
            'username': user.username,
            'active': user.is_active,
            'my_post': Post.objects.filter(author=user),
        }

    return render(request, 'users/profile.html', context)