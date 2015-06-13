# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Pf(models.Model):
    UID = models.ForeignKey('Users', db_column='UID')  # Field name made lowercase.
    PID = models.CharField(db_column='PID', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PF'
        unique_together = (('UID', 'PID'),)


class PfValue(models.Model):
    uid = models.ForeignKey('Users', db_column='UID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PF_VALUE'


class Players(models.Model):
    pid = models.CharField(db_column='PID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYERS'


class PlayerVals(models.Model):
    pid = models.ForeignKey(Players, db_column='PID', primary_key=True)  # Field name made lowercase.
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYER_VALS'


class Stats(models.Model):
    PID = models.ForeignKey(Players, db_column='PID')  # Field name made lowercase.
    GAMEID = models.CharField(db_column='GAMEID', max_length=20)  # Field name made lowercase.
    points = models.IntegerField(db_column='POINTS', blank=True, null=True)  # Field name made lowercase.
    steals = models.IntegerField(db_column='STEALS', blank=True, null=True)  # Field name made lowercase.
    rebounds = models.IntegerField(db_column='REBOUNDS', blank=True, null=True)  # Field name made lowercase.
    assists = models.IntegerField(db_column='ASSISTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATS'
        unique_together = (('GAMEID', 'PID'),)


class Users(models.Model):
    uid = models.CharField(db_column='UID', primary_key=True, max_length=20)  # Field name made lowercase.
    pfid = models.CharField(db_column='PFID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'USERS'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.ForeignKey(AuthGroup)
    permission_id = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.ForeignKey(AuthUser)
    group_id = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.ForeignKey(AuthUser)
    permission_id = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
