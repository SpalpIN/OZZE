# Generated by Django 3.0.8 on 2020-07-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozze_app', '0003_auto_20200715_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='session_key',
            field=models.CharField(max_length=40),
        ),
    ]