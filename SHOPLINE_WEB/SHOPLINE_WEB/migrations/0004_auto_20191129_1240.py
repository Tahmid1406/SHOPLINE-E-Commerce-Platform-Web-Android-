# Generated by Django 2.1.5 on 2019-11-29 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SHOPLINE_WEB', '0003_auto_20191122_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
