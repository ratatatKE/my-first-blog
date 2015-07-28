from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
# import to help with login

from django.contrib.auth.decorators import login_required

# import data form the Post Model
from .models import Post
# to take the actual blog posts from the Post Model we need something called a query set

# add a new view for creating the posts
from .forms import *

def pure_css_tut(request):
	return render(request, 'blog/purecss.html')

# Create your views here.
# this is the simplest view
def post_list(request):
    # get the posts from the database
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # to pass posts to the user, we will pass it to the template as views {'posts':posts}
    return render(request, 'blog/post_list.html', {'posts': posts})


# we have a new view called post detail, it is getting a variable called pk
def post_detail(request, pk):
    # we want to get one and only one object from our blog post
    post = get_object_or_404(Post, pk=pk)
    # return it to the client
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
def post_edit(request, pk):
    '''
    notice the extra pk parameter from the url
    '''
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        '''
        we pass the post object as instance bothw when we start the form and when we edit the form
        '''
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


@login_required
# create a new view for our drafts page
def post_draft_list(request):
    # makes sure we take only unpublished posts
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # calling the publish method on the post
    post.publish()
    return redirect('blog.views.post_detail', pk=pk)


@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')


def add_comment_to_post(request, pk):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=pk)
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)
