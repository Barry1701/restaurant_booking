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

    