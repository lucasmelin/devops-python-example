# Generated by Django 2.1.2 on 2020-12-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20181124_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='decimals',
            field=models.IntegerField(default=2),
        ),
    ]