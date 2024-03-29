# Generated by Django 3.2.23 on 2024-02-11 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_logs_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='description',
            field=models.CharField(default='Novas Mudanças chegaram ao RetiNode!', max_length=255, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='discussions',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Imagem do post'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='logs',
            name='image',
            field=models.FileField(upload_to='', verbose_name='Imagem'),
        ),
    ]
