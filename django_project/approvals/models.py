from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import logging
logr = logging.getLogger(__name__)

class Notification(models.Model):
        title = models.CharField(max_length=100)
        message = models.TextField()
        viewed = models.BooleanField(default=False)
        user = models.ForeignKey(User, on_delete=models.CASCADE)

#notification will be show at the time when user is created
def create_welcome_message(sender, **kwargs):
        if kwargs['created']:
                notification = Notification.objects.create(user=kwargs['instance'],
                                                title="Welcome",
                                                message="Thanks for signing up!"
                                                )

post_save.connect(create_welcome_message, sender=User)

