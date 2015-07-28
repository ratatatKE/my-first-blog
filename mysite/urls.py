import contacts.views
from django.conf.urls import include, url, patterns
from django.contrib import admin

#
admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    ## this is our login url
    # url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'', include('blog.urls')),

    #     This is for the login page
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),

    # we are using class based notation hence the .as_view() since we dont want a string back
    # url(r'^$', contacts.views.ListContactView.as_view(), name='contacts-list'),
]
