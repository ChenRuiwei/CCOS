# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'address'


class Administrator(models.Model):
    administrator_id = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=20)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'administrator'


class Business(models.Model):
    business_id = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'business'


class Canteen(models.Model):
    canteen_id = models.AutoField(primary_key=True)
    administrator = models.ForeignKey(Administrator, models.DO_NOTHING)
    canteen_name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'canteen'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'category'


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', models.DO_NOTHING)
    contact_name = models.CharField(max_length=50)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'contact'


class Customer(models.Model):
    customer_id = models.CharField(primary_key=True, max_length=10)
    password = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'customer'


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey('Restaurant', models.DO_NOTHING)
    category = models.ForeignKey(Category, models.DO_NOTHING)
    dish_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    photo_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dish'


class Indent(models.Model):
    indent_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, models.DO_NOTHING)
    address = models.ForeignKey(Address, models.DO_NOTHING)
    contact = models.ForeignKey(Contact, models.DO_NOTHING)
    order_time = models.DateTimeField()
    state = models.DecimalField(max_digits=1, decimal_places=0)
    order_notes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'indent'


class IndentDish(models.Model):
    indent = models.OneToOneField(Indent, models.DO_NOTHING, primary_key=True)  # The composite primary key (indent_id, dish_id) found, that is not supported. The first column is selected.
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    dish_number = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'indent_dish'
        unique_together = (('indent', 'dish'),)


class Restaurant(models.Model):
    restaurant_id = models.AutoField(primary_key=True)
    canteen = models.ForeignKey(Canteen, models.DO_NOTHING)
    business = models.ForeignKey(Business, models.DO_NOTHING)
    restaurant_name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.DecimalField(max_digits=11, decimal_places=0)
    photo_url = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restaurant'
