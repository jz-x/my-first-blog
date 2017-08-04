# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 10:46:37 2017

@author: Jerry
"""

from django.conf.urls import url
from . import views

urlpatterns = [ url(r'^$', views.post_list, name='post_list'), 
               url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),]
