# Generated by Django 3.0.3 on 2020-07-15 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kurstar', '0008_passed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passed',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kurstar.Course'),
        ),
    ]
