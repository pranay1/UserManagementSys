# Generated by Django 2.2.8 on 2019-12-19 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deviceDetail', '0010_auto_20191219_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='parameters',
            field=models.CharField(default='Pass dictionary here', max_length=1000),
        ),
    ]