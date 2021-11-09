from django.contrib import admin

from .models import MeetingRoom, Reservation, User

# Register your models here.
admin.site.register(User)
admin.site.register(Reservation)
admin.site.register(MeetingRoom)