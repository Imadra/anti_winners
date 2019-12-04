from django.db import models

# Create your models here.
class Auditory(models.Model):
    capacity = models.IntegerField(null=True)
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
        return self.id