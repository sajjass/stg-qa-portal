# Generated by Django 2.0.4 on 2018-04-27 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailystatus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystats',
            name='Description',
            field=models.TextField(max_length=5000),
        ),
    ]
