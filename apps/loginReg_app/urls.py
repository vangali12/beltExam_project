from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
# FORMS
	url(r'^$', views.logRegUserPage),
	url(r'^friends$', views.dashUserPage),
	url(r'^users/show/(?P<id>\d+)$', views.profilePage),

# USER ACTIONS
	url(r'^loginUser$', views.loginUser),
	url(r'^create$', views.createUser),
	url(r'^deleteRelationship/(?P<id>\d+)$', views.deleteRelationship),
	url(r'^createRelationship/(?P<id>\d+)$', views.createRelationship),
	url(r'^logout$', views.logout),

]