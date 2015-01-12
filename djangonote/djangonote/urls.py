from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangonote.views import home_view

urlpatterns = patterns('',
	url(r'^$', home_view, name='home'),
    url(r'^notes/', include('notes.urls', namespace='notes')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': 'home'}, name='logout'), 
)
