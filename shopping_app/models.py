# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class all_products(models.Model):
    product_id = models.AutoField(primary_key=True, db_column='product_id')
    product_name = models.CharField(db_column='Product_Name', max_length=20, blank=True, null=True)  # Field name made lowercase.
    product_description = models.CharField(max_length=50, db_column='product_description', blank=True, null=True)
    product_image = models.ImageField(upload_to='product_images/', db_column='product_image')
    product_mrp = models.IntegerField(db_column='product_mrp', blank=True, null=True)
    product_price = models.IntegerField(db_column='product_price', blank=True, null=True)
    product_category = models.CharField(max_length=20, db_column='product_category', blank=True, null=True)
    product_sub_category = models.CharField(max_length=20, db_column='product_sub_category', blank=True, null=True)
    product_specification_1 = models.CharField(max_length=20, db_column='product_specification_1', blank=True, null=True)
    product_specification_2 = models.CharField(max_length=20, db_column='product_specification_2', blank=True, null=True)
    product_gender = models.CharField(max_length=10, db_column='product_gender', blank=True, null=True)
    product_stock_available = models.IntegerField(db_column='product_stock_available', blank=True, null=True)
    product_rating = models.CharField(max_length=30, db_column='product_rating', blank=True, null=True)
    product_total_sold = models.IntegerField(db_column='product_total_sold', blank=True, null=True)
    product_is_trusted = models.CharField(max_length=10, db_column='product_is_trusted', blank=True, null=True)
    product_review_id = models.IntegerField(db_column='product_review_id', blank=True, null=True)
    product_status = models.CharField(max_length=10,db_column='product_status', blank=True, null=True)


class All_products_in_bag(models.Model):
    bag_id = models.AutoField(primary_key=True, db_column='bag_id')
    bag_customer_id = models.IntegerField(db_column='bag_customer_id')
    bag_product_id = models.IntegerField(db_column='bag_product_id')
    bag_quantity = models.IntegerField(db_column='bag_quantity')
    total_price = models.IntegerField(db_column='total_price')


class Company_Info(models.Model):
    company_logo = models.ImageField(upload_to='company_logo/', db_column='company_logo')
    company_name = models.CharField(max_length=10, db_column='company_name')
    company_description = models.CharField(max_length=10, db_column='company_description')


class Country(models.Model):
    country_id = models.CharField(max_length=50, db_column='country_id')
    country_name = models.CharField(max_length=50, db_column='country_name')
    country_is_active = models.CharField(max_length=50, db_column='country_is_active')


class Customer(models.Model):
    customer_username = models.CharField(max_length=20, db_column='customer_username', blank=True, null=True)
    customer_password = models.CharField(max_length=15, db_column='customer_password', blank=True, null=True)
    customer_first_name = models.CharField(max_length=10, db_column='customer_first_name', blank=True, null=True)
    customer_last_name = models.CharField(max_length=10, db_column='customer_last_name', blank=True, null=True)
    customer_phone_number = models.CharField(max_length=40,db_column='customer_phone_number', blank=True, null=True)
    customer_alternative_phone_number = models.CharField(max_length=40,db_column='customer_alternative_phone_number', blank=True, null=True)
    customer_email = models.CharField(max_length=20, db_column='customer_email', blank=True, null=True)
    customer_building_id = models.CharField(max_length=20, db_column='customer_building_id', blank=True, null=True)
    customer_landmark = models.CharField(max_length=20, db_column='customer_landmark', blank=True, null=True)
    customer_street = models.CharField(max_length=20, db_column='customer_street', blank=True, null=True)
    customer_city = models.CharField(max_length=20, db_column='customer_city', blank=True, null=True)
    customer_country = models.CharField(max_length=20, db_column='customer_country', blank=True, null=True)
    customer_pincode = models.CharField(max_length=20, db_column='customer_pincode', blank=True, null=True)
    customer_total_buyed = models.CharField(max_length=20, db_column='customer_total_buyed', blank=True, null=True)
    customer_status = models.CharField(max_length=20, db_column='customer_status', blank=True, null=True)


class Orders(models.Model):
    order_customer_id = models.IntegerField(db_column='order_customer_id')
    order_product_id = models.IntegerField(db_column='order_product_id')
    order_quantity = models.IntegerField(db_column='order_quantity')
    order_total_price = models.IntegerField(db_column='order_total_price')
    order_ordered_time = models.CharField(max_length=10, db_column='order_ordered_time')
    order_expected_time = models.CharField(max_length=10, db_column='order_expected_time')
    order_delivery_status = models.CharField(max_length=20, db_column='order_delivery_status')


class ReviewTable(models.Model):
    review_id = models.AutoField(primary_key=True, db_column='review_id')
    review_customer_id = models.IntegerField(db_column='review_customer_id')
    review_content = models.CharField(max_length=100, db_column='review_content')


class banner(models.Model):
    banner_name = models.CharField(max_length=50, db_column='banner_name')
    banner_img = models.ImageField(upload_to='banner/', db_column='banner_img')
