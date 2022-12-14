# Generated by Django 4.1 on 2022-09-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_products',
            fields=[
                ('product_id', models.AutoField(db_column='product_id', primary_key=True, serialize=False)),
                ('product_name', models.CharField(db_column='Product_Name', max_length=20)),
                ('product_description', models.CharField(db_column='product_description', max_length=50)),
                ('product_image', models.ImageField(db_column='product_image', upload_to='product_images/')),
                ('product_mrp', models.IntegerField(db_column='product_mrp')),
                ('product_price', models.IntegerField(db_column='product_price')),
                ('product_category', models.CharField(db_column='product_category', max_length=20)),
                ('product_sub_category', models.CharField(db_column='product_sub_category', max_length=20)),
                ('product_specification_1', models.CharField(db_column='product_specification_1', max_length=20)),
                ('product_specification_2', models.CharField(db_column='product_specification_2', max_length=20)),
                ('product_gender', models.CharField(db_column='product_gender', max_length=10)),
                ('product_stock_available', models.IntegerField(db_column='product_stock_available')),
                ('product_rating', models.CharField(db_column='product_rating', max_length=30)),
                ('product_total_sold', models.IntegerField(db_column='product_total_sold')),
                ('product_is_trusted', models.CharField(db_column='product_is_trusted', max_length=10)),
                ('product_review_id', models.IntegerField(db_column='product_review_id')),
            ],
        ),
        migrations.CreateModel(
            name='All_products_in_bag',
            fields=[
                ('bag_id', models.AutoField(db_column='bag_id', primary_key=True, serialize=False)),
                ('bag_customer_id', models.IntegerField(db_column='bag_customer_id')),
                ('bag_product_id', models.IntegerField(db_column='bag_product_id')),
                ('bag_quantity', models.IntegerField(db_column='bag_quantity')),
                ('total_price', models.IntegerField(db_column='total_price')),
            ],
        ),
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_name', models.CharField(db_column='banner_name', max_length=50)),
                ('banner_img', models.ImageField(db_column='banner_img', upload_to='banner/')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_logo', models.CharField(db_column='company_logo', max_length=60)),
                ('company_name', models.CharField(db_column='company_name', max_length=10)),
                ('company_description', models.CharField(db_column='company_description', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_id', models.CharField(db_column='country_id', max_length=50)),
                ('country_name', models.CharField(db_column='country_name', max_length=50)),
                ('country_is_active', models.CharField(db_column='country_is_active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_username', models.CharField(db_column='customer_username', max_length=20)),
                ('customer_password', models.CharField(db_column='customer_password', max_length=15)),
                ('customer_first_name', models.CharField(db_column='customer_first_name', max_length=10)),
                ('customer_last_name', models.CharField(db_column='customer_last_name', max_length=10)),
                ('customer_phone_number', models.IntegerField(db_column='customer_phone_number')),
                ('customer_alternative_phone_number', models.IntegerField(db_column='customer_alternative_phone_number')),
                ('customer_email', models.CharField(db_column='customer_email', max_length=20)),
                ('customer_building_id', models.CharField(db_column='customer_building_id', max_length=20)),
                ('customer_landmark', models.CharField(db_column='customer_landmark', max_length=20)),
                ('customer_street', models.CharField(db_column='customer_street', max_length=20)),
                ('customer_city', models.CharField(db_column='customer_city', max_length=20)),
                ('customer_country', models.CharField(db_column='customer_country', max_length=20)),
                ('customer_pincode', models.CharField(db_column='customer_pincode', max_length=20)),
                ('customer_total_buyed', models.CharField(db_column='customer_total_buyed', max_length=20)),
                ('customer_status', models.CharField(db_column='customer_status', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_customer_id', models.IntegerField(db_column='order_customer_id')),
                ('order_product_id', models.IntegerField(db_column='order_product_id')),
                ('order_quantity', models.IntegerField(db_column='order_quantity')),
                ('order_total_price', models.IntegerField(db_column='order_total_price')),
                ('order_ordered_time', models.CharField(db_column='order_ordered_time', max_length=10)),
                ('order_expected_time', models.CharField(db_column='order_expected_time', max_length=10)),
                ('order_delivery_status', models.CharField(db_column='order_delivery_status', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewTable',
            fields=[
                ('review_id', models.AutoField(db_column='review_id', primary_key=True, serialize=False)),
                ('review_customer_id', models.IntegerField(db_column='review_customer_id')),
                ('review_content', models.CharField(db_column='review_content', max_length=100)),
            ],
        ),
    ]
