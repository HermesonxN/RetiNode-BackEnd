# Generated by Django 3.2.23 on 2024-02-16 20:37

import Api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_auto_20240213_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussions',
            name='image',
            field=models.ImageField(upload_to=Api.models.upload_image_discussion, verbose_name='Imagem do post'),
        ),
    ]
