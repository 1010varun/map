# Generated by Django 4.2.5 on 2023-09-21 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authUser', '0002_customuser_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='location',
        ),
        migrations.AddField(
            model_name='customuser',
            name='latitude',
            field=models.FloatField(default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='longitude',
            field=models.FloatField(default=0.0, null=True),
        ),
    ]
