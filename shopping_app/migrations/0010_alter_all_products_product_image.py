# Generated by Django 4.1 on 2022-09-21 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping_app', '0009_alter_all_products_product_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_products',
            name='product_image',
            field=models.ImageField(db_column='product_image', default='the pic', upload_to='product_images/'),
            preserve_default=False,
        ),
    ]