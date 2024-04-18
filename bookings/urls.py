from django.urls import path
from .views import BookingFormView, BookingListView, ThanksView

urlpatterns = [
    path('create/', BookingFormView.as_view(), name='create_booking'),#for creating booking
    path('list/',  BookingListView.as_view(), name='booking_list'),#for listing booking
    path('thanks/', ThanksView.as_view(), name='thanks'),

]