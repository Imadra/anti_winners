from django.contrib import admin

# Register your models here.
from .models import Auditory, Booking

admin.site.register(Auditory)
admin.site.register(Booking)