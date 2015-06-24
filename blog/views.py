from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

#import data form the Post Model
from .models import Post
#to take the actual blog posts from the Post Model we need something called a query set

#add a new view for creating the posts
from .forms import PostForm

# Create your views here.
#this is the simplest view
def post_list(request):
	#get the posts from the database
	posts= Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
 	#to pass posts to the user, we will pass it to the template as views {'posts':posts}
 	return render(request, 'blog/post_list.html', {'posts':posts})

 	#we have a new view called post detail, it is getting a variable called pk 
def post_detail(request, pk):
 	#we want to get one and only one object from our blog post
 	post=get_object_or_404(Post, pk=pk)
	#return it to the client
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	#separate the logic according to request type, either get or post
	if request.method== "POST":
		#construct the postform with data from the form
		form=PostForm(request.POST)
		#checj to see if form is valid
		if form.is_valid():
			post=form.save(commit=False) #means you dont' want to save the post model yet
			post.author=request.user
			post.published_date=timezone.now()
			post.save()
			#reditect the user to the post detail page for the created post
			return redirect('blog.views.post_detail', pk=post.pk)
		elif request.method== "GET":
			#to create a new form we call PostForm() and pass it to the template
			form=PostForm()

	return render(request,'blog/post_edit.html', {'form': form})

def post_edit(request, pk): 
	'''
	notice the extra pk parameter from the url
	'''
	post= get_object_or_404(Post, pk=pk)
	if request.method=="POST":
		form=PostForm(request.POST, instance=post)
		'''
		we pass the post object as instance bothw when we start the form and when we edit the form
		'''
		if form.is_valid():
			post=form.save(commit=False)
			post.author=request.user
			post.published_date=timezone.now()
			post.save()

			return redirect('blog.views.post_detail', pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form':form})