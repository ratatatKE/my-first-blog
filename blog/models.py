from django.db import models
from django.utils import timezone

# Create your models here.

# this is a model for our blog post, always start a class name with an upper letter
class Post(models.Model):
    """docstring for Post"""
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # method for publishing the blog post in the post model
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


# this is a class for the comments model
class Comment(models.Model):
    # the related_name= allows us to have access to comments right from the Post model
    post = models.ForeignKey('blog.post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved=True)
