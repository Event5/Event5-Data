# Generated by Django 3.1 on 2020-08-29 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0005_auto_20200828_0903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='associates',
        ),
        migrations.RemoveField(
            model_name='event',
            name='conferences',
        ),
        migrations.RemoveField(
            model_name='event',
            name='public',
        ),
        migrations.AddField(
            model_name='event',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='organization',
            name='url',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='usere',
            name='email',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
