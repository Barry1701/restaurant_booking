# from django.http import HttpResponse
# from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import BookingForm
from .models import Booking





# Create your views here.
class BookingFormView(LoginRequiredMixin, generic.FormView):
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



class BookingListView(LoginRequiredMixin, generic.ListView):
    template_name = 'bookings/booking_list.html'
    context_object_name = 'bookings'

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

class ThanksView(generic.TemplateView):
    template_name = 'bookings/thanks.html'

def fetch_availability_view(request):
    # Available dates and time slots from data base
    availability_data = {
        'available_dates': ['2024-04-20', '2024-04-21'],
        'time_slots': {
            '2024-04-20': ['09:00', '12:00', '18:00'],
            '2024-04-21': ['11:00', '15:00'],
        }
    }

    return JsonResponse(availability_data)

   
class HomeView(generic.TemplateView):
    template_name = 'bookings/booking_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('create_booking')
        else:
            return redirect(reverse_lazy('account_login'))