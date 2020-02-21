from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, update_session_auth_hash
from django.contrib import messages
from .form import SignUpForm, SignInForm, UpdateUserForm, ChangeUserPassword, UpdateProfileForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.models import User
from ticketing.models import Event, EventParticipant

from .models import Profile

# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('registration:home'))

def home_view(request):
    if  request.user.is_active:
        if request.user.is_authenticated:
            profile = Profile.objects.get(id=request.user.id)
            event_active = EventParticipant.objects.filter(user=request.user, invoice__pay_status = True)
        else :
            profile = None
        context = {
            'profile' : profile,
            'event_active' : event_active
        }
        return render(request, 'dash.html', context)
    else :
        return render(request, 'home.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()
            # email = form.clean_email()
            # username = form.cleaned_data.get('username')
            new_user = authenticate(username=user.username, password=password)
            login(request, new_user)
            return HttpResponseRedirect(reverse('registration:home'))
    else:
        form = SignUpForm()
    
    context = {
        'form' : form
    }
    return render(request, 'signup.html', context)

def signin_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registration:home'))
    else:
        form = SignInForm(request.POST)
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username = username, password = password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('registration:home'))
                else:
                    return HttpResponse("Your account is inactive")
            else:
                print("Someone tried to login and failed")
                print("He used username : {}, password : {}".format(username, password))
                messages.error(request,'username atau password salah')
                return HttpResponseRedirect(reverse('registration:sign_in'))
        else:
            form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, 'signin.html', context)

def edit_user_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        form = UpdateUserForm(instance = user)
        if user.is_authenticated:
            if request.method == 'POST':
                form = UpdateUserForm(request.POST, instance=user)

                if form.is_valid:
                    update = form.save(commit = False)
                    update.save()
                return HttpResponse('Confirm')
        else:
            form = UpdateUserForm(instance = user)
        context = {
            'form' : form
        }
        return render(request, 'edit_user.html', context)
    else:
        return HttpResponseRedirect(reverse('registration:home'))

def edit_password_view(request):
    if request.user.is_authenticated:
        form = ChangeUserPassword(request.POST)
        if request.method == 'POST':
            new_password = request.POST.get('new_password1')
            old_password = request.POST.get('old_password')
            username = request.user.username

            user = authenticate(username=username, password=old_password)

            if user:
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
                return HttpResponseRedirect(reverse('registration:home'))
            else :
                return HttpResponse('Password lama salah')
        else:
            form = ChangeUserPassword()
        context = {
            'form' : form
        }
        return render(request, 'change_password.html', context)
    else:
        return HttpResponseRedirect(reverse('registration:home'))

def edit_profile_view(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        profile = user.profile
        form = UpdateProfileForm(instance=profile)

        if user.is_authenticated:
            if request.method == 'POST':
                form = UpdateProfileForm(request.POST, request.FILES, instance=profile)
                if form.is_valid:
                    update = form.save(commit = False)
                    update.user = user
                    update.save()
                return HttpResponseRedirect(reverse('registration:profile'))
        else:
            form = UpdateProfileForm(instance=profile)
        context ={
            'form' :form,
            'profile' :profile
        }
        return render(request, 'edit_profile.html', context)
    else:
        return HttpResponseRedirect(reverse('registration:home'))

def profile_view(request):
    user = User.objects.get(id=request.user.id)
    profile = user.profile

    context = {
        'user' : user,
        'profile' : profile
    }

    return render(request, 'profile_view.html', context)


