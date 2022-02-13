from .models import CrawlStatus, PubmedDatabase,Tag
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import messages
from .forms import SignUpForm, EditProfileForm
from .data_populate import ToDatabase
import os

def tag_article(request,id_name):
    if not request.user.is_authenticated:
        return render(request, 'authenticate/login.html',{})
    else:
        if request.method =="POST":
            tag_value =request.POST.get('tags')
            tag, _ = Tag.objects.get_or_create(tag_name=tag_value, user=request.user)
            article = PubmedDatabase.objects.get(id_name=id_name)
            article.tags.add(tag)
            article.save()

            return render(request, 'authenticate/tag_article.html',{})

# Create your views here.

def home(request):
    status,iscreated = CrawlStatus.objects.get_or_create(status = False)
    if iscreated:
        ToDatabase()
    return render(request, 'authenticate/home.html',{})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, ('You Have Been Logged In!'))
            return redirect('home')
        else:
            messages.success(request, ('Something went wrong! Please try again.'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})     

def logout_user(request):
    logout(request)
    messages.success(request, ('You have been succesfully logged out.'))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username= username, password=password)
            login(request,user)
            messages.success(request,('You have succesfully registered.'))
            return redirect('home')
    else:
        form = SignUpForm()
        
    context = {'form': form}
    return render(request, 'authenticate/register.html',context)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,('You have succesfully edited your profile.'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)
        
    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html',context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,('You have succesfully changed your password.'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
        
    context = {'form': form}
    return render(request, 'authenticate/change_password.html',context)

def search_results(request):
    if request.method == "POST":
        searched = request.POST['searched']
        article = PubmedDatabase.objects.filter(abstracts__contains=searched)
        return render(request, 'authenticate/search_result.html',{'searched':searched,'article':article})
    else:
        return render(request, 'authenticate/search_result.html',{})


def tagged_articles(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            user_tags = Tag.objects.filter(user=request.user)

            taggeds = PubmedDatabase.objects.none()

            for user_tag in user_tags:
                taggeds |= PubmedDatabase.objects.filter(tags=user_tag)
        
            return render(request, 'authenticate/tagged_articles.html',{'tagged_articles':taggeds})

    return render(request, 'authenticate/tagged_articles',{})


