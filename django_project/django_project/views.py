from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
	LoginView,
	PasswordResetView,
	PasswordResetDoneView,
	PasswordResetConfirmView
)
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import RegistrationForm
from approvals.models import Notification
from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponse("This is view")
@login_required
def redir(request):
    return HttpResponse("This is view")

class PasswordReset(PasswordResetView):
	template_name = 'registration/password_reset_form.html'

class PasswordResetDone(PasswordResetDoneView):
	template_name = 'registration/password_reset_done.html'

class PasswordResetConfirm(PasswordResetConfirmView):
	template_name = "registration/password_reset_confirm.html"

def login(request):
        context = {}
        context.update(csrf(request))
        return render(request, 'login.html', context)

def auth_view(request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
                auth.login(request, user)
                return HttpResponseRedirect("/accounts/loggedin")
        else:
                return HttpResponse("Not Logged")

#notification will only be shown the first time, make viewed=True to view it every timme on login
def loggedin(request):
	ns = Notification.objects.values()
	n = Notification.objects.filter(user=request.user, viewed=False)
	print(ns)
	print(n)
	return render(request, 'loggedin.html', {'full_name':request.user.username, 'notifications': n})

def invalid(request):
        return HttpResponse("Invalid")

def logout(request):
        auth.logout(request)
        return HttpResponseRedirect("/accounts/login")

def register_user(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Registered")
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/register.html', args)

def register_success(request):
	return render(request, "register_success.html")

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            HttpResponseRedirect("/accounts/register_success")
        else:
            HttpResponseRedirect("accounts/register/")
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


