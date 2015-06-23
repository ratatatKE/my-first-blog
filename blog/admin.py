from django.contrib import admin
#to add edit and delete posts, we need to import the Model we created
from .models import Post

# Register your models here.

#thic code here serves to make our model visible on the admin page, so we are practically registering the model
admin.site.register(Post)
