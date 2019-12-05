from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


def calc_bool_coef(aviable, req, coef):
    if not coef:
        return 0
    if req is None or req == aviable:
        return coef
    return 0


def calc_num_coef(aviable, req, coef):
    if not coef:
        return 0
    if not req:
        return coef
    return min(aviable/req, 1.0) * coef


class Auditory(models.Model):
    capacity = models.IntegerField(null=True)
    has_projector = models.BooleanField(default=False)
    has_whiteboard = models.BooleanField(default=False)
    volume = models.IntegerField(null=True, default=0)
    has_air_conditioning = models.BooleanField(default=False)
    has_noise_isolation = models.BooleanField(default=False)
    computer_count = models.IntegerField(default=0)
    micro_count = models.IntegerField(default=0)
    has_internet = models.BooleanField(default=False)
    has_speakers = models.BooleanField(default=False)
    room_number = models.CharField(max_length=20, default="No title", unique=True)

    def __str__(self):
        return str(self.id)

    def __hash__(self):
        return int(self.id)

    def __eq__(self, other):
        return other.id == self.id

    def __cmp__(self, other):
        return self.id > other.id


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time_from = models.DateTimeField(default=datetime.now)
    time_till = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=50, default="conduct hackathon")

    capacity = models.IntegerField(null=True, blank=True)
    computer_count = models.IntegerField(null=True, blank=True)
    micro_count = models.IntegerField(null=True, blank=True)
    has_projector = models.BooleanField(null=True, blank=True)
    has_whiteboard = models.BooleanField(null=True, blank=True)
    volume = models.IntegerField(null=True, blank=True)
    has_air_conditioning = models.BooleanField(null=True, blank=True)
    has_noise_isolation = models.BooleanField(null=True, blank=True)
    has_internet = models.BooleanField(null=True, blank=True)
    has_speakers = models.BooleanField(null=True, blank=True)

    capacity_coef = models.FloatField(null=True, blank=True)
    has_projector_coef = models.FloatField(null=True, blank=True)
    has_whiteboard_coef = models.FloatField(null=True, blank=True)
    volume_coef = models.FloatField(null=True, blank=True)
    has_air_conditioning_coef = models.FloatField(null=True, blank=True)
    has_noise_isolation_coef = models.FloatField(null=True, blank=True)
    computer_count_coef = models.FloatField(null=True, blank=True)
    micro_count_coef = models.FloatField(null=True, blank=True)
    has_internet_coef = models.FloatField(null=True, blank=True)
    has_speakers_coef = models.FloatField(null=True, blank=True)

    auditory = models.ForeignKey(Auditory, on_delete=models.CASCADE, null=True, blank=True)
    edge_weight = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.id)

    def calculate_edge_with(self, auditory):
        res = 0
        div = 0

        res += calc_num_coef(auditory.capacity, self.capacity, self.capacity_coef)
        if self.capacity_coef:
            div += self.capacity_coef

        res += calc_num_coef(auditory.computer_count, self.computer_count, self.computer_count_coef)
        if self.computer_count_coef:
            div += self.computer_count_coef

        res += calc_bool_coef(auditory.micro_count, self.micro_count, self.micro_count_coef)
        if self.micro_count_coef:
            div += self.micro_count_coef

        res += calc_bool_coef(auditory.has_projector, self.has_projector, self.has_projector_coef)
        if self.has_projector_coef:
            div += self.has_projector_coef

        res += calc_bool_coef(auditory.has_whiteboard, self.has_whiteboard, self.has_whiteboard_coef)
        if self.has_whiteboard_coef:
            div += self.has_whiteboard_coef

        res += calc_bool_coef(auditory.volume, self.volume, self.volume_coef)
        if self.volume_coef:
            div += self.volume_coef

        res += calc_bool_coef(auditory.has_air_conditioning, self.has_air_conditioning, self.has_air_conditioning_coef)
        if self.has_air_conditioning_coef:
            div += self.has_air_conditioning_coef

        res += calc_bool_coef(auditory.has_noise_isolation, self.has_noise_isolation, self.has_noise_isolation_coef)
        if self.has_noise_isolation_coef:
            div += self.has_noise_isolation_coef

        res += calc_bool_coef(auditory.has_internet, self.has_internet, self.has_internet_coef)
        if self.has_internet_coef:
            div += self.has_internet_coef

        res += calc_bool_coef(auditory.has_speakers, self.has_speakers, self.has_speakers_coef)
        if self.has_speakers_coef:
            div += self.has_speakers_coef
        if div == 0:
            return 1
        res /= div
        return res

    def set_auditory(self, auditory):
        self.auditory = auditory
        self.edge_weight = self.calculate_edge_with(self.auditory)
        self.save()

    def to_external(self):
        return {
            ''
        }

    def __str__(self):
        return str(self.id)

    def __hash__(self):
        return int(self.id)

    def __eq__(self, other):
        return other.id == self.id

    def __cmp__(self, other):
        return self.id > other.id
