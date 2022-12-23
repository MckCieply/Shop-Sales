# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Names(models.Model):
    product_id = models.AutoField(primary_key=True, blank=True, null=False)
    name = models.TextField(blank=True, null=True)
    brand = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'names'


class Sales(models.Model):
    sale_id = models.AutoField(primary_key=True, blank=True, null=False)
    product = models.OneToOneField('Stock', models.DO_NOTHING, blank=True, null=True)
    old_price = models.IntegerField(blank=True, null=True)
    sale_percent = models.IntegerField(blank=True, null=True)
    new_price = models.IntegerField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sales'


class Stock(models.Model):
    product_id = models.AutoField(primary_key=True, blank=True, null=False)
    price = models.IntegerField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    updated = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock'
