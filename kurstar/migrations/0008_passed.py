# Generated by Django 3.0.3 on 2020-07-15 12:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kurstar', '0007_lesson_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurstar.Lesson')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Прохождение',
                'verbose_name_plural': 'Прохождения',
            },
        ),
    ]
