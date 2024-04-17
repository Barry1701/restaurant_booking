from django.contrib import admin
from .models import Booking

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_dispaly = ('date', 'time', 'number_of_guests', 'user')

