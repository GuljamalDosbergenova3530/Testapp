# Generated by Django 4.2.3 on 2023-07-20 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luck', '0007_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d/'),
        ),
    ]