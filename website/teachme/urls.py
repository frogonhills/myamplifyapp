#!/usr/bin/python

from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^post/$',views.post),
	url(r'^signin/$',views.signin),
	url(r'^signup/$',views.signup),
	url(r'^profile/$',views.profile),
	
	
	
]


urlpatterns += staticfiles_urlpatterns()