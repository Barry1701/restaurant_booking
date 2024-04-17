from django.contrib import admin
from .models import Booking
from .models import TimeSlot

# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'number_of_guests', 'user')

admin.site.register(TimeSlot)

