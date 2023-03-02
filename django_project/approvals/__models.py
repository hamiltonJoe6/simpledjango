from django.db import models
from approvals.signals import article_approved
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

@receiver(post_save, sender=User)
def create_welcome_message(sender, **kwargs):
        if kwargs.get('created', False):
                Notification.objects.create(user=kwargs.get('instance'),
                                                title="Welcome",
                                                message="Thanks for signing up!"
                                                )


class Approval(models.Model):
	approved = models.BooleanField(default=False)
	article_id = models.IntegerField()

	def save(self, **kwargs):
		if self.id is not None and self.approved == True:
			rec = article_approved.send(self, article_id=self.article_id)
			logr.debug("Approval confirmed for article id = %s" % self.article_id)

			super(Approval, self).save(kwargs)


