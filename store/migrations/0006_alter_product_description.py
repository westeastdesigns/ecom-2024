# Generated by Django 5.0.6 on 2024-05-11 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1500, null=True),
        ),
    ]
