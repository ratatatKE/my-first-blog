from django.conf.urls import url
from . import views

#add our first url pattern

urlpatterns = [
		#an empty string will match for here
		url(r'^$', views.post_list),
		# this is a url for viewing only one post
		url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
		# ^ is the beginning
		#after the beginnign the url should contain the word post
		# (?P<pk>[0-9]+) Django should collect everything here and transfer it to the view as a variable called pk
		#0-9 it can only be anomber
		# + there needs to be one oe more digits
		#$ means the end

		#this is the line to create new posts
		url(r'^post/new/$', views.post_new, name='post_new'),

		#this is the url for editing
		url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit')

]