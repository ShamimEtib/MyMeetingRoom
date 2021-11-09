from django import forms
from API.models import MeetingRoom

class CreateRoomModelForm(forms.ModelForm):
    class Meta:
        model = MeetingRoom
        fields = ['room_number', 'capacity']