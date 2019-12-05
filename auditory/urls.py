from django.urls import path
from .views import AddAuditory, Distribute, AddBooking, GetReservations

urlpatterns = [
    path('add_auditory/', AddAuditory.as_view()),
    path('distribute/', Distribute.as_view()),
    path('add_booking/', AddBooking.as_view()),
    path('get_reservations/', GetReservations.as_view())
]
