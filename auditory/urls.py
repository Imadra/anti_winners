from django.urls import path
from .views import Ping# , Register, CheckToken, login

urlpatterns = [
    path('ping/', Ping.as_view()),
]