# Generated by Django 4.1 on 2022-09-21 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0008_all_products_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='product_status',
            field=models.CharField(blank=True, db_column='product_status', max_length=10, null=True),
        ),
    ]
