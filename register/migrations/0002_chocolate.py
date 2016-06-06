# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, verbose_name='Name', blank=True)),
                ('description', models.CharField(max_length=100, null=True, verbose_name='Description', blank=True)),
                ('manufacturer', models.CharField(max_length=100, null=True, verbose_name='Manufacturer', blank=True)),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, verbose_name='Chocolate Price', validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
