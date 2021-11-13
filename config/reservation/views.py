from http.client import responses
from django import template
from django.db.models import query
from django.forms import forms
from django.shortcuts import render, get_object_or_404,redirect
from django.template import response
from rest_framework.response import Response
from API.models import Reservation, User, MeetingRoom
from django.contrib.auth import get_user_model

from django.contrib.auth.decorators import login_required
import requests

from reservation.forms import CreateReservationModelForm



def reservation_list_view(request):
    if request.GET.get('room-filter'):
        room_number = MeetingRoom.objects.get(room_number=request.GET.get('room-filter'))
        queryset = Reservation.objects.filter(room_number=room_number)
    elif request.GET.get('user-filter'):
        username = get_user_model().objects.get(username = request.GET.get('user-filter'))
        queryset = Reservation.objects.filter(reservation_user=username)
    else:
        queryset = Reservation.objects.all()
    room_list = MeetingRoom.objects.all()
    user_list = get_user_model().objects.all()
    title = "Reservation list"
    template_name = 'reservation/list.html'
    context = {
        'title': title,
        'object_list': queryset,
        'room_list': room_list,
        'user_list': user_list
    }
    return render(request, template_name, context)

@login_required
def reservation_create_view(request):
    template_name = 'reservation/create.html'
    form = CreateReservationModelForm(request.POST or None)
    if form.is_valid():
        if request.method == 'POST':
            data = request.POST.copy()
            user = request.user
            data.update({'reservation_user': int(user.id)})
            response = requests.post(
                'http://localhost:8000/api/reservation/', data=data)
            content = response.content
            return redirect('/')
    context = {
        "title": "Create new reservation",
        "form": form
    }
    return render(request, template_name, context)
        

def reservation_detail_view(request, id, *room_number):
    title = "Details of " + str(room_number) + " meeting room"
    obj = get_object_or_404(Reservation, id=id)
    template_name = 'reservation/detail.html'
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)

@login_required
def reservation_update_view(request, *room_number, id):
    title = "Updating " + str(room_number) + " room reservation"
    obj = get_object_or_404(Reservation, id=id)
    form = CreateReservationModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    template_name = 'reservation/create.html'
    context = {
        'title': title,
        'object': obj,
        'form': form,
    }
    return render(request, template_name, context)


@login_required
def reservation_delete_view(request, *room_number, id):
    title = "Deleting " + str(room_number) + " meeting room"
    obj = get_object_or_404(Reservation, id=id)
    template_name = 'reservation/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect('/')
    context = {
        'title': title,
        'object': obj
    }
    return render(request, template_name, context)