# Generated by Django 4.1.4 on 2022-12-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subcategory',
        ),
        migrations.AddField(
            model_name='product',
            name='sub_category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='S', upload_to='shop/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='0'),
        ),
    ]
