from django.conf.urls import url
from . import views

# add our first url pattern

urlpatterns = [
    # an empty string will match for here
    url(r'^$', views.post_list),
    url(r'^purecss/$', views.pure_css_tut),
    # this is a url for viewing only one post, takes the url, and the view to be rendered
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),

    # ^ is the beginning
    # after the beginnign the url should contain the word post
    # (?P<pk>[0-9]+) Django should collect everything here and transfer it to the view as a variable called pk
    # 0-9 it can only be anomber
    # + there needs to be one oe more digits
    # $ means the end


    # this is the line to create new posts
    url(r'^post/new/$', views.post_new, name='post_new'),

    # this is the url for editing
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    # this is a url for unpublished posts
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', views.post_publish, name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove'),

]
