# from django.http import HttpResponse
# from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView

from .forms import BookingForm
from .models import Booking




# Create your views here.
class BookingFormView(LoginRequiredMixin, FormView):
    template_name = 'bookings/booking_form.html'
    form_class = BookingForm
    success_url = reverse_lazy('thanks') #redirect to thanks page


    def form_valid(self, form):
        # Associate the booking with the logged-in user
        booking = form.save(commit=False)
        booking.user = self.request.user
        booking.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return self.success_url



class BookingListView(LoginRequiredMixin, ListView):
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class ThanksView(TemplateView):
    template_name = 'bookings/thanks.html'