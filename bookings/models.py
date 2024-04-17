from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Booking(models.Model):
    date = models.DateField()
    time = models.TimeField()
    number_of_guests = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Booking #{self.pk} - {self.date} at {self.time} for {self.number_of_guests} guests"

class TimeSlot(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f" {self.date} - {self.start_time} to {self.end_time}"