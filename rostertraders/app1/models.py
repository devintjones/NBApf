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





class Players(models.Model):
    pid = models.CharField(db_column='PID', primary_key=True, max_length=20)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    team = models.CharField(db_column='TEAM', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYERS'


class PlayerVals(models.Model):
    pid = models.ForeignKey(Players,db_column='PID',primary_key=True)
    value = models.FloatField(db_column='VALUE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PLAYER_VALS'


class Stats(models.Model):
    pid = models.ForeignKey(Players,db_column='pid')
    gameid = models.CharField(db_column='gameid',max_length=20, blank=True, null=True)
    points = models.IntegerField(db_column='POINTS', blank=True, null=True)  # Field name made lowercase.
    steals = models.IntegerField(db_column='STEALS', blank=True, null=True)  # Field name made lowercase.
    rebounds = models.IntegerField(db_column='REBOUNDS', blank=True, null=True)  # Field name made lowercase.
    assists = models.IntegerField(db_column='ASSISTS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATS'


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
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


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
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)



class Pf(models.Model):
    user   = models.ForeignKey(SocialAuthUsersocialauth,db_column='user')
    pid    = models.ForeignKey(Players,db_column='pid')
    id     = models.CharField(db_column='id',primary_key=True, max_length=20)
    shares = models.IntegerField(db_column="shares")

    # calculated field
    @property
    def player_pf_val(self):
        return self.shares * PlayerVals.objects.filter(pid=self.pid.pid)[0].value
    
    class Meta:
        managed = False
        db_table = 'PF'


class PfValue(models.Model):
    user = models.ForeignKey(Pf,db_column='user',primary_key=True)
    #assets = models.FloatField(db_column='assets', blank=True, null=True)  # Field name made lowercase.
    cash = models.FloatField(db_column='cash')

    @property
    def assets(self):
	return sum([player.player_pf_val for player in Pf.objects.filter(user=0).all()])

    @property
    def net_worth(self):
        return self.assets + self.cash

    class Meta:
        managed = False
        db_table = 'PF_VALUE'
