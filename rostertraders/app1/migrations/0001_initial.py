# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(null=True, blank=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, serialize=False, primary_key=True)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PID', models.CharField(max_length=20, db_column='PID')),
            ],
            options={
                'db_table': 'PF',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('pid', models.CharField(max_length=20, serialize=False, primary_key=True, db_column='PID')),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('team', models.CharField(max_length=255, null=True, db_column='TEAM', blank=True)),
            ],
            options={
                'db_table': 'PLAYERS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('GAMEID', models.CharField(max_length=20, db_column='GAMEID')),
                ('points', models.IntegerField(null=True, db_column='POINTS', blank=True)),
                ('steals', models.IntegerField(null=True, db_column='STEALS', blank=True)),
                ('rebounds', models.IntegerField(null=True, db_column='REBOUNDS', blank=True)),
                ('assists', models.IntegerField(null=True, db_column='ASSISTS', blank=True)),
            ],
            options={
                'db_table': 'STATS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uid', models.CharField(max_length=20, serialize=False, primary_key=True, db_column='UID')),
                ('pfid', models.CharField(max_length=20, null=True, db_column='PFID', blank=True)),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('email', models.CharField(max_length=255, null=True, db_column='EMAIL', blank=True)),
                ('pw', models.CharField(max_length=255, null=True, db_column='PW', blank=True)),
            ],
            options={
                'db_table': 'USERS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PfValue',
            fields=[
                ('uid', models.ForeignKey(primary_key=True, db_column='UID', serialize=False, to='app1.Users')),
                ('value', models.FloatField(null=True, db_column='VALUE', blank=True)),
            ],
            options={
                'db_table': 'PF_VALUE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerVals',
            fields=[
                ('pid', models.ForeignKey(primary_key=True, db_column='PID', serialize=False, to='app1.Players')),
                ('value', models.FloatField(null=True, db_column='VALUE', blank=True)),
            ],
            options={
                'db_table': 'PLAYER_VALS',
                'managed': False,
            },
        ),
    ]
