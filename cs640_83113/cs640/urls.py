from django.conf.urls import patterns, url, include

from cs640 import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
)
