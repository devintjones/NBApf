from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^players',views.player_vals, name='player_vals'),
	url(r'^$', views.index, name='index'),
	    ]

