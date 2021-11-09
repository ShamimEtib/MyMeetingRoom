from django import forms
from django.forms import fields, models
from API.models import Reservation


class CreateReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'room_number',
            'reservation_date',
            'reservation_time',
            'reservation_duration',
            'id',
        ]