from django.urls import path
from . import views
    
urlpatterns = [
    path('create/', views.BookingFormView.as_view(), name='create_booking'),
    path('list/',  views.BookingListView.as_view(), name='booking_list'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('fetch_availability/', views.fetch_availability_view, name='fetch_availabilisty'),
   
]