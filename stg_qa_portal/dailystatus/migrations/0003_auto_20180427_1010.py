# Generated by Django 2.0.4 on 2018-04-27 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailystatus', '0002_auto_20180427_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailystats',
            name='defects_filed',
            field=models.CharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='dailystats',
            name='defects_verified',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]