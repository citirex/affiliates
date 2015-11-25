# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.db import models


class AdvCategory(models.Model):
    name = models.CharField(max_length=75)
    image = models.ImageField(upload_to='adv_categories/', blank=True, null=True)

    def __str__(self):
        return self.name

    @property
    def get_subcategories(self):
        return self.advsubcategory_set.all()


class AdvSubCategory(models.Model):
    name = models.CharField(max_length=75)
    category = models.ForeignKey(AdvCategory)

    def __str__(self):
        return self.name
