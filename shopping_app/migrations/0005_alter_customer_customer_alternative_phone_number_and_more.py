# Generated by Django 4.1 on 2022-09-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0004_alter_company_info_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_alternative_phone_number',
            field=models.IntegerField(blank=True, db_column='customer_alternative_phone_number', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_building_id',
            field=models.CharField(blank=True, db_column='customer_building_id', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_city',
            field=models.CharField(blank=True, db_column='customer_city', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_country',
            field=models.CharField(blank=True, db_column='customer_country', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_email',
            field=models.CharField(blank=True, db_column='customer_email', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_first_name',
            field=models.CharField(blank=True, db_column='customer_first_name', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_landmark',
            field=models.CharField(blank=True, db_column='customer_landmark', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_last_name',
            field=models.CharField(blank=True, db_column='customer_last_name', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_password',
            field=models.CharField(blank=True, db_column='customer_password', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_phone_number',
            field=models.IntegerField(blank=True, db_column='customer_phone_number', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_pincode',
            field=models.CharField(blank=True, db_column='customer_pincode', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.CharField(blank=True, db_column='customer_status', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_street',
            field=models.CharField(blank=True, db_column='customer_street', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_total_buyed',
            field=models.CharField(blank=True, db_column='customer_total_buyed', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_username',
            field=models.CharField(blank=True, db_column='customer_username', max_length=20, null=True),
        ),
    ]