# Generated by Django 3.0.3 on 2020-08-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurstar', '0012_auto_20200807_0531'),
    ]

    operations = [
        migrations.AddField(
            model_name='callbacks',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='callbacks',
            name='called',
            field=models.BooleanField(default=False, verbose_name='Обработано'),
        ),
    ]
