from django.shortcuts import render
from django.utils import timezone
#import data form the Post Model
from .models import Post
#to take the actual blog posts from the Post Model we need something called a query set


# Create your views here.
#this is the simplest view
def post_list(request):
	#get the posts from the database
	posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 	#to pass posts to the user, we will pass it to the template as views {'posts':posts}
 	return render(request, 'blog/post_list.html', {'posts':posts})