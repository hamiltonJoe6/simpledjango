from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
from PIL import Image
from django.dispatch import receiver

class StuProfileManager(models.Manager):
	def get_queryset(self):
		return super(StuProfileManager, self).get_queryset().filter(title='hey')

class Stu(models.Model):
	stusobjects = models.Manager()
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
	slug = models.SlugField(unique=True)
	title = models.CharField(max_length=100)
	content = models.TextField()
	likes = models.IntegerField(default=0)
	approved = models.BooleanField(default=False)
	image = models.ImageField(
		null=True,
		blank=True,
		width_field="width_field",
		height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)

	hey = StuProfileManager()

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("Stu:detailpost", kwargs={"slug": self.slug})

def create_approval_on_new_article(sender, **kwargs):
	if kwargs['created']:
		approval = Approval.objects.create(article_id=kwargs.get('instance').id)
		print(approval)

post_save.connect(create_approval_on_new_article, sender=Stu)

class Comment(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField()
	article = models.ForeignKey(Stu, on_delete=models.CASCADE)

	def __str__(self):
                return self.name

def create_slug(instance, new_slug=None):
	slug = slugify(instance.title)
	if new_slug is not None:
		slug = new_slug
	qs = Stu.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, sender=Stu)


class Post(models.Model):
	post = models.CharField(max_length=200)
