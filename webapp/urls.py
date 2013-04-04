#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'^idea/(?P<idea_id>\d+)/up/$', views.up, name='up'),
    url(r'^idea/(?P<idea_id>\d+)/down/$', views.down, name='down'),
    url(r'^idea/(?P<idea_id>\d+)/delete/$', views.delete, name='delete'),
    url(r'^dashboard$', views.dashboard, name='dashboard'),
    url(r'^login$', views.do_login, name='login'),
    url(r'^logout$', views.quit, name='logout'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^new$', views.new_idea, name='newidea'),
    )
