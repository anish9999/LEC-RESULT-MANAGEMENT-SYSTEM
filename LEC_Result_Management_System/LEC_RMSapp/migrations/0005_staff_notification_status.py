# Generated by Django 4.0.2 on 2022-03-03 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LEC_RMSapp', '0004_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
