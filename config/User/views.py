from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
import requests
from django.contrib.auth import authenticate,login,logout
from API.models import Reservation
from .forms import CreateUserModelForm, LoginUserModelForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from django.contrib.auth.models import User


def user_create_view(request):
    form = CreateUserModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            username = request.POST.get('username')
            password = request.POST.get('password')
            response = requests.post(
                'http://localhost:8000/api/users/', data=data)
            #content = response.content
            user = authenticate(username=username, password=password)
            login(request,user)
            return redirect('/')
    context = {
        "title": "Create new user",
        "form": form
    }
    return render(request, 'User/create.html', context)


@csrf_exempt
def user_login_view(request):
    form = LoginUserModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            # data = request.POST.copy()
            username = request.POST.get('username')
            csrt_token = request.POST.get('csrfmiddlewaretoken')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            # print(data)
            #print(csrt_token)
            response = requests.post(
                'http://localhost:8000/api/api-auth/login/', data={'username': username, 'password': password}, headers={'csrftoken': csrt_token}, cookies={'csrftoken': csrt_token}
            )
            if user is not None:
                login(request,user)
                return redirect('/')
            else:
                messages.info(request,'UserName or password is incorrect')
    context = {
        "title": "Login to your user",
        "form": form
    }
    return render(request, 'User/login.html', context)

def user_logout_view(request):
    logout(request)
    return redirect('/user/login')