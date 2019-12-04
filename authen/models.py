from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100, blank=True)

#the profile will automatically change in db whenever user changes
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# '''
# <h2>{{ user.get_full_name }}</h2>
# <ul>
#   <li>Username: {{ user.username }}</li>
#   <li>Location: {{ user.profile.location }}</li>
#   <li>Birth Date: {{ user.profile.birth_date }}</li>
# </ul>
#
#
# def update_profile(request, user_id):
#     user = User.objects.get(pk=user_id)
#     user.profile.bio = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit...'
#     user.save()
#
#
# '''