# Generated by Django 3.0.3 on 2020-09-07 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurstar', '0015_course_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='language',
            field=models.CharField(default='kk', max_length=20, verbose_name='Язык'),
        ),
    ]
