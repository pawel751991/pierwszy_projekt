# Generated by Django 3.2.4 on 2021-07-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sklint', '0003_alter_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='Zdjęcia'),
        ),
    ]