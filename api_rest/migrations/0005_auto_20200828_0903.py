# Generated by Django 3.1 on 2020-08-28 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0004_auto_20200828_0749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='user_id',
        ),
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(db_table='user_event', related_name='users', to='api_rest.UserE'),
        ),
    ]
