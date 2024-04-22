from django.urls import path
from . import views
from allauth.account.views import LoginView, LogoutView, SignupView 
    
urlpatterns = [
    path('create/', views.BookingFormView.as_view(), name='create_booking'),
    path('list/',  views.BookingListView.as_view(), name='booking_list'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('fetch_availability/', views.fetch_availability_view, name='fetch_availabilisty'),
    path('login/', LoginView.as_view(), name='login'),  # Widok logowania
    path('logout/', LogoutView.as_view(), name='logout'),  # Widok wylogowania
    path('register/', SignupView.as_view(), name='register'),
]