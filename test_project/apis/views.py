from apis.models import PubmedDatabase
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,PasswordChangeForm
from django.contrib import messages
from apis.forms import SignUpForm, EditProfileForm
import os



# Create your views here.
def home(request):
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