from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class CriteriaCategory(models.Model):
#     name = models.CharField(max_length=40)
#     possible_values = models.CharField(max_length=500)
#     coef = models.FloatField(null=True)
#
#
# class CriteriaNumber(models.Model):
#     coef = models.FloatField(null=True)


class Auditory(models.Model):
    capacity = models.IntegerField(null=True)
    # criteria = models.ManyToManyField()
    has_projector = models.BooleanField()
    has_whiteboard = models.BooleanField()
    volume = models.IntegerField(null=True)
    has_air_conditioning = models.BooleanField()
    has_noise_isolation = models.BooleanField()
    computer_count = models.IntegerField()
    micro_count = models.IntegerField()
    has_internet = models.BooleanField()
    has_speakers = models.BooleanField()
    color = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_from = models.DateTimeField()
    time_till = models.DateTimeField()

    has_projector = models.BooleanField()
    has_whiteboard = models.BooleanField()
    volume = models.IntegerField(null=True)
    has_air_conditioning = models.BooleanField()
    has_noise_isolation = models.BooleanField()
    computer_count = models.IntegerField()
    micro_count = models.IntegerField()
    has_internet = models.BooleanField()
    has_speakers = models.BooleanField()
    color = models.CharField(max_length=20)

    has_projector_coef = models.FloatField()
    has_whiteboard_coef = models.FloatField()
    volume_coef = models.FloatField()
    has_air_conditioning_coef = models.FloatField()
    has_noise_isolation_coef = models.FloatField()
    computer_count_coef = models.FloatField()
    micro_count_coef = models.FloatField()
    has_internet_coef = models.FloatField()
    has_speakers_coef = models.FloatField()
    color_coef = models.FloatField(max_length=20)


    def __str__(self):
        return str(self.id)

    # def calculate(self):
