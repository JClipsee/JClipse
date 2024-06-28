from django.contrib import admin
from .models import Photographer, Client, Appointment, Offers

# Register your models here.

admin.site.register(Photographer)
admin.site.register(Client)
admin.site.register(Appointment)
admin.site.register(Offers)
