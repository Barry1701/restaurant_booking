from django.urls import path
from .views import BookingFormView, BookingListView, ThanksView, fetch_availability_view, UserRegistrationView, UserLoginView, UserLogoutView



urlpatterns = [
    path('create/', BookingFormView.as_view(), name='create_booking'),#for creating booking
    path('list/',  BookingListView.as_view(), name='booking_list'),#for listing booking
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('fetch_availability/', fetch_availability_view, name='fetch_availabilisty'),
    path('register/', UserRegistrationView.as_view(), name='register'), # For user registration
    path('login/', UserLoginView.as_view(), name='login'), # For user login
    path('logout/', UserLogoutView.as_view(), name='logout'), # For user logout

]