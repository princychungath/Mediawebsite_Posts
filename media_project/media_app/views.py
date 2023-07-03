from django.shortcuts import render
from .models import Post
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import login, logout
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .forms import PostForm


def home(request):
    return render(request, 'base.html')



def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home') 
            else:
                form.add_error(None, 'Invalid credentials. Please try again.')  
    else:
        form = UserLoginForm()
    return render(request, 'media_app/signin.html', {'form': form})
    


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'media_app/signup.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect('home') 


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_posts')
    else:
        form = PostForm()
    return render(request, 'media_app/addpost.html', {'form': form})

@login_required
def view_posts(request):
    posts=Post.objects.all()
    return render(request, 'media_app/viewpost.html', {'posts': posts})

@login_required
def detail_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'media_app/post_detail.html', {'post': post})

@login_required
def delete(request,post_id):
    post=get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('view_posts')


@login_required
def update(request,post_id):
    post=get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('view_posts')
    else:
        form = PostForm(instance=post)
    return render(request, 'media_app/update.html', {'form': form})
