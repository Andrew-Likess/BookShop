# Generated by Django 4.2.4 on 2023-08-17 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookItems', '0002_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=6),
        ),
    ]
