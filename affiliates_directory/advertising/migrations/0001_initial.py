# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('image', models.ImageField(null=True, upload_to='adv_categories/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AdvSubCategory',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('category', models.ForeignKey(to='advertising.AdvCategory')),
            ],
        ),
    ]
