from django.db import models
from django.utils import timezone

# Create your models here.

#this is a model for our blog post, always start a class name with an upper letter
class Post(models.Model):
	"""docstring for Post"""
	author= models.ForeignKey('auth.User')
	title= models.CharField(max_length=200)
	text=models.TextField()
	created_date=models.DateTimeField(default=timezone.now)
	published_date=models.DateTimeField(blank=True, null=True)

	#method for publishing the blog post in the post model
	def publish(self):
		self.published_date=timezone.now()
		self.save()

	def __str__(self):
		return self.title