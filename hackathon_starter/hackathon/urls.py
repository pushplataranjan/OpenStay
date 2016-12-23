from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from hackathon import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetView)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^api/$', views.api_examples, name='api'),
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^twitter/$', views.twitter, name='twitter'),
    url(r'^twitterTweets/$', views.twitterTweets, name='twitterTweets'),
    url(r'^twitter_login/$', views.twitter_login, name='twitter_login'),
    url(r'^facebook_login/$', views.facebook_login, name='facebook_login'),
    url(r'^facebook/$', views.facebook, name='facebook'),
    url(r'^google_login/$', views.google_login, name='google_login'),
    url(r'^google/$', views.googlePlus, name='googlePlus')
)
