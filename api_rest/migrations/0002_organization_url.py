# Generated by Django 3.1 on 2020-08-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='url',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]