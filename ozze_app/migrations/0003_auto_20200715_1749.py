# Generated by Django 3.0.8 on 2020-07-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozze_app', '0002_auto_20200715_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartmodel',
            name='session_key',
            field=models.CharField(max_length=40, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='cartmodel',
            unique_together=set(),
        ),
    ]
