# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        regex=r'^categories/$',
        view=views.AdvCategoryView.as_view(),
        name='categories'
    ),
    url(r'^$', views.HomeView.as_view(), name="home"),

]
