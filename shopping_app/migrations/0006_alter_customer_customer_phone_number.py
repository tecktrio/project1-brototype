# Generated by Django 4.1 on 2022-09-20 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0005_alter_customer_customer_alternative_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_phone_number',
            field=models.IntegerField(blank=True, db_column='customer_phone_number', max_length=40, null=True),
        ),
    ]
