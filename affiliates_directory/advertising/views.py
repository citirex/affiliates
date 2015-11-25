# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.views.generic import View, TemplateView
from .models import *


class AdvCategoryView(TemplateView):
    template_name = 'advertising/advcategory.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AdvCategoryView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['advcat_list'] = AdvCategory.objects.all()
        return context


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(HomeView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['advcat_list'] = AdvCategory.objects.all()
        return context
