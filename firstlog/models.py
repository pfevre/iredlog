# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Maddr(models.Model):
    partition_tag = models.IntegerField(blank=True, null=True)
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'maddr'


class Mailaddr(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    priority = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'mailaddr'


class Msgrcpt(models.Model):
    partition_tag = models.IntegerField()
    mail_id = models.CharField(max_length=16)
    rseqnum = models.IntegerField()
    rid = models.BigIntegerField()
    is_local = models.CharField(max_length=1)
    content = models.CharField(max_length=1)
    ds = models.CharField(max_length=1)
    rs = models.CharField(max_length=1)
    bl = models.CharField(max_length=1, blank=True)
    wl = models.CharField(max_length=1, blank=True)
    bspam_level = models.FloatField(blank=True, null=True)
    smtp_resp = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'msgrcpt'


class Msgs(models.Model):
    partition_tag = models.IntegerField()
    mail_id = models.CharField(max_length=16)
    secret_id = models.CharField(max_length=16, blank=True)
    am_id = models.CharField(max_length=20)
    time_num = models.IntegerField()
    time_iso = models.CharField(max_length=16)
    sid = models.BigIntegerField()
    policy = models.CharField(max_length=255, blank=True)
    client_addr = models.CharField(max_length=255, blank=True)
    size = models.IntegerField()
    originating = models.CharField(max_length=1)
    content = models.CharField(max_length=1, blank=True)
    quar_type = models.CharField(max_length=1, blank=True)
    quar_loc = models.CharField(max_length=255, blank=True)
    dsn_sent = models.CharField(max_length=1, blank=True)
    spam_level = models.FloatField(blank=True, null=True)
    message_id = models.CharField(max_length=255, blank=True)
    from_addr = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    host = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'msgs'


class OutboundWblist(models.Model):
    rid = models.IntegerField()
    sid = models.IntegerField()
    wb = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'outbound_wblist'


class Policy(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    policy_name = models.CharField(unique=True, max_length=255)
    virus_lover = models.CharField(max_length=1, blank=True)
    spam_lover = models.CharField(max_length=1, blank=True)
    unchecked_lover = models.CharField(max_length=1, blank=True)
    banned_files_lover = models.CharField(max_length=1, blank=True)
    bad_header_lover = models.CharField(max_length=1, blank=True)
    bypass_virus_checks = models.CharField(max_length=1, blank=True)
    bypass_spam_checks = models.CharField(max_length=1, blank=True)
    bypass_banned_checks = models.CharField(max_length=1, blank=True)
    bypass_header_checks = models.CharField(max_length=1, blank=True)
    virus_quarantine_to = models.CharField(max_length=64, blank=True)
    spam_quarantine_to = models.CharField(max_length=64, blank=True)
    banned_quarantine_to = models.CharField(max_length=64, blank=True)
    unchecked_quarantine_to = models.CharField(max_length=64, blank=True)
    bad_header_quarantine_to = models.CharField(max_length=64, blank=True)
    clean_quarantine_to = models.CharField(max_length=64, blank=True)
    archive_quarantine_to = models.CharField(max_length=64, blank=True)
    spam_tag_level = models.FloatField(blank=True, null=True)
    spam_tag2_level = models.FloatField(blank=True, null=True)
    spam_tag3_level = models.FloatField(blank=True, null=True)
    spam_kill_level = models.FloatField(blank=True, null=True)
    spam_dsn_cutoff_level = models.FloatField(blank=True, null=True)
    spam_quarantine_cutoff_level = models.FloatField(blank=True, null=True)
    addr_extension_virus = models.CharField(max_length=64, blank=True)
    addr_extension_spam = models.CharField(max_length=64, blank=True)
    addr_extension_banned = models.CharField(max_length=64, blank=True)
    addr_extension_bad_header = models.CharField(max_length=64, blank=True)
    warnvirusrecip = models.CharField(max_length=1, blank=True)
    warnbannedrecip = models.CharField(max_length=1, blank=True)
    warnbadhrecip = models.CharField(max_length=1, blank=True)
    newvirus_admin = models.CharField(max_length=64, blank=True)
    virus_admin = models.CharField(max_length=64, blank=True)
    banned_admin = models.CharField(max_length=64, blank=True)
    bad_header_admin = models.CharField(max_length=64, blank=True)
    spam_admin = models.CharField(max_length=64, blank=True)
    spam_subject_tag = models.CharField(max_length=64, blank=True)
    spam_subject_tag2 = models.CharField(max_length=64, blank=True)
    spam_subject_tag3 = models.CharField(max_length=64, blank=True)
    message_size_limit = models.IntegerField(blank=True, null=True)
    banned_rulenames = models.CharField(max_length=64, blank=True)
    disclaimer_options = models.CharField(max_length=64, blank=True)
    forward_method = models.CharField(max_length=64, blank=True)
    sa_userconf = models.CharField(max_length=64, blank=True)
    sa_username = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'policy'


class Quarantine(models.Model):
    partition_tag = models.IntegerField()
    mail_id = models.CharField(max_length=16)
    chunk_ind = models.IntegerField()
    mail_text = models.TextField()

    class Meta:
        managed = False
        db_table = 'quarantine'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    priority = models.IntegerField()
    policy_id = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    fullname = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wblist(models.Model):
    rid = models.IntegerField()
    sid = models.IntegerField()
    wb = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'wblist'
