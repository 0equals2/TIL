from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm
from .models import User
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect("posts:index")
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('posts:index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login(request):
    if request.user.is_authenticated:
        return redirect("posts:index")
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('posts:index')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout(request):
    auth_logout(request)
    return redirect("posts:index")

def user_page(request, user_id):
    user_info = User.objects.get(id=user_id)
    context = {
        'user_info': user_info
    }
    return render(request, 'accounts/user_page.html', context)

def follow(request, user_id):
    me = request.user
    you = User.objects.get(id=user_id)

    if me != you:
        # if you in me.follow.all():
        #     me.follow.remove(you)
        # else:
        #     me.follow.add(you)
        if me in you.follower.all():
            you.follower.remove(me)
        else:
            you.follower.add(me)
    return redirect('accounts:user_page', user_id)




