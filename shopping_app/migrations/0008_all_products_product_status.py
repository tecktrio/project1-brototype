# Generated by Django 4.1 on 2022-09-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0007_alter_customer_customer_alternative_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='all_products',
            name='product_status',
            field=models.IntegerField(blank=True, db_column='product_status', null=True),
        ),
    ]
