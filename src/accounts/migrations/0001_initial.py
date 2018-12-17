# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-17 00:53
from __future__ import unicode_literals

import accounts.choices
import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('avatar', models.ImageField(blank=True, upload_to=accounts.models.user_directory_path)),
                ('nickname', models.CharField(blank=True, db_index=True, default=b'', help_text='User Nickname', max_length=32, null=True, verbose_name='Nickname')),
                ('bio', models.TextField(blank=True, default=b'', help_text='User Bio', null=True, verbose_name=b'Bio')),
                ('gender', models.CharField(choices=[(accounts.choices.Gender((0,)), 'Other'), (accounts.choices.Gender((1,)), 'Female'), (accounts.choices.Gender((2,)), 'Male')], default=accounts.choices.Gender((0,)), help_text='User Gender', max_length=2, verbose_name='Gender')),
                ('birthday', models.DateField(blank=True, db_index=True, help_text='User Birthday', null=True, verbose_name='Birthday')),
                ('receive_newsletters', models.BooleanField(default=False, help_text='I would like to receive Email Updates', verbose_name='I would like to receive Email Updates')),
                ('is_newly_created', models.BooleanField(default=True)),
                ('user', models.OneToOneField(help_text='User', on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'ordering': ['user__first_name', 'user__last_name'],
                'verbose_name': 'user profile',
                'verbose_name_plural': 'user profiles',
            },
        ),
    ]
