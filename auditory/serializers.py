from rest_framework import serializers
from .models import Auditory, Booking

class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditory
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'