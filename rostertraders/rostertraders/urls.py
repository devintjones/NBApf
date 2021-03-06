"""rostertraders URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf.urls.static import static


urlpatterns = [
	#url(r'^login/$', 'django.contrib.auth.views.login'),
	#url(r'^logout/$', 'django.contrib.auth.views.logout'),
	url(r'^players','app1.views.player_vals'),
	url(r'^$', 'app1.views.index'),
	url('', include('social.apps.django_app.urls', namespace='social')),
	url(r'^home/$',   'app1.views.home'),
	url(r'^contact/$','app1.views.contact'),
	url(r'^logout/$', 'app1.views.logout'),
	url(r'^sell_shares/$', 'app1.views.sell_shares'),
	url(r'^buy_shares/$', 'app1.views.buy_shares'),
	url(r'^admin/', include(admin.site.urls)),
]
