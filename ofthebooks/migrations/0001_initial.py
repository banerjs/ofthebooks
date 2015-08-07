# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookReview',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=500)),
                ('author', models.CharField(max_length=500)),
                ('rating', models.IntegerField(blank=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], null=True)),
                ('amazon_url', models.URLField(max_length=1000, blank=True, null=True)),
                ('amazon_image_url', models.URLField(max_length=1000, blank=True, null=True)),
                ('review', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=1000, unique=True, editable=False, blank=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
