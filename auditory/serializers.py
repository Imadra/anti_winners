from rest_framework import serializers
from .models import Auditory

class AuditorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Auditory
        fields = '__all__'