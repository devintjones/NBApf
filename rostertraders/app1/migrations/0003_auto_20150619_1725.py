# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_customuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='App1Customuser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'app1_customuser',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthAssociation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.CharField(max_length=255)),
                ('handle', models.CharField(max_length=255)),
                ('secret', models.CharField(max_length=255)),
                ('issued', models.IntegerField()),
                ('lifetime', models.IntegerField()),
                ('assoc_type', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'social_auth_association',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthCode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.CharField(max_length=254)),
                ('code', models.CharField(max_length=32)),
                ('verified', models.IntegerField()),
            ],
            options={
                'db_table': 'social_auth_code',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthNonce',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server_url', models.CharField(max_length=255)),
                ('timestamp', models.IntegerField()),
                ('salt', models.CharField(max_length=65)),
            ],
            options={
                'db_table': 'social_auth_nonce',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialAuthUsersocialauth',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(max_length=32)),
                ('uid', models.CharField(max_length=255)),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'social_auth_usersocialauth',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
