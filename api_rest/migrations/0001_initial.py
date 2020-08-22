# Generated by Django 3.1 on 2020-08-21 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('event_start_date', models.DateTimeField()),
                ('template', models.CharField(max_length=100)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.event')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('biography', models.TextField()),
                ('role', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=100)),
                ('photo_url', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
                ('type_user', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=150)),
                ('user_status', models.CharField(max_length=10)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleSpeakers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.schedule')),
                ('speaker_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.speaker')),
            ],
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('event_id', models.ManyToManyField(related_name='registrys', to='api_rest.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='api_rest.user')),
            ],
        ),
        migrations.CreateModel(
            name='EventData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('header_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('background_url', models.CharField(max_length=255)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ManyToManyField(related_name='events', to='api_rest.User'),
        ),
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('logo_url', models.CharField(max_length=255)),
                ('event_id', models.ManyToManyField(related_name='associates', to='api_rest.Event')),
            ],
        ),
    ]
