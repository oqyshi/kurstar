# Generated by Django 3.0.7 on 2020-06-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurstar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс', 'verbose_name_plural': 'Курстар'},
        ),
        migrations.AlterModelOptions(
            name='lesson',
            options={'verbose_name': 'Сабақ', 'verbose_name_plural': 'Сабақтар'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='course',
            name='banner',
            field=models.ImageField(default='asdfgh', upload_to='courses_banners/', verbose_name='Изображение для блока'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(verbose_name='Описание курса'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название курса'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='number',
            field=models.IntegerField(default=0, verbose_name='Номер урока'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название урока'),
        ),
    ]
