from django.urls import path
from .views import AddAuditory, Distribute

urlpatterns = [
    path('add_auditory/', AddAuditory.as_view()),
    path('distribute/', Distribute.as_view()),
]
