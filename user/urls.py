from django.conf.urls import url
#from django.urls import path
from user import views

urlpatterns = [
	  url(r'/(?P<id>[0-9]+)$', views.edition, name = 'edition'),
]