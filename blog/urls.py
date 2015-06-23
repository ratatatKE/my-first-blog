from django.conf.urls import url
from . import views

#add our first url pattern

urlpatterns = [
		#an empty string will match for here
		url(r'^$', views.post_list),
]