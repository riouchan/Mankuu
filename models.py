# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class DevTable(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    insert_date = models.DateTimeField()
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dev_table'


class DjangoContentType(models.Model):
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class ManqooRelations(models.Model):
    customer_code = models.CharField(unique=True, max_length=10, blank=True, null=True)
    parking_name = models.CharField(max_length=255, blank=True, null=True)
    database = models.CharField(max_length=100, blank=True, null=True)
    start_rack = models.IntegerField(blank=True, null=True)
    end_rack = models.IntegerField(blank=True, null=True)
    machine_id = models.IntegerField(blank=True, null=True)
    area_code = models.IntegerField(blank=True, null=True)
    available_flag = models.IntegerField(blank=True, null=True)
    empty_threshold = models.IntegerField(blank=True, null=True)
    busy_threshold = models.IntegerField(blank=True, null=True)
    vehicle_type = models.IntegerField(blank=True, null=True)
    full_car_count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)
    machine_type = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manqoo_relations'
