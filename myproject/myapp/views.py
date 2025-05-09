from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 

from .forms import SignupForm, LoginForm, BlogForm

from .models import Blog

def index(request):
    return render(request, 'index.html')


def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    error_message = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('create_blog') 
            else:
                form = LoginForm()
                error_message = 'Invalid username or password'
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form,'error': error_message})


def user_logout(request):
    logout(request)
    return redirect('login')


def create_blog(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create_blog') 
    blogs = Blog.objects.all()
    return render(request, 'create_blog.html', {'form': form, 'blogs': blogs}) 