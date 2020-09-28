# Generated by Django 3.0.8 on 2020-07-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ozze_app', '0007_auto_20200717_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='coatmodel',
            name='type',
            field=models.CharField(default='Coat', max_length=4, verbose_name='Не менять'),
        ),
        migrations.AddField(
            model_name='dressmodel',
            name='type',
            field=models.CharField(default='Dress', max_length=5, verbose_name='Не менять'),
        ),
        migrations.AddField(
            model_name='facemaskmodel',
            name='type',
            field=models.CharField(default='Face_mask', max_length=9, verbose_name='Не менять'),
        ),
        migrations.AddField(
            model_name='parkamodel',
            name='type',
            field=models.CharField(default='Parka', max_length=5, verbose_name='Не менять'),
        ),
        migrations.AlterField(
            model_name='coatmodel',
            name='picture',
            field=models.ImageField(upload_to='coat', verbose_name='Главная картинка'),
        ),
    ]
