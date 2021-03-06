# Generated by Django 3.1 on 2020-08-25 21:37

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
                ('template', models.IntegerField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date_time', models.DateTimeField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.event')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.CreateModel(
            name='UserE',
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
            options={
                'db_table': 'user',
            },
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
                ('schedule_id', models.ManyToManyField(db_table='shedule_speaker', related_name='Schedule', to='api_rest.Schedule')),
            ],
            options={
                'db_table': 'speaker',
            },
        ),
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('event_id', models.ManyToManyField(db_table='event-registry', related_name='registrys', to='api_rest.Event')),
            ],
            options={
                'db_table': 'registry',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('date_modification', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organizations', to='api_rest.usere')),
            ],
            options={
                'db_table': 'organization',
            },
        ),
        migrations.CreateModel(
            name='EventData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_url', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=100)),
                ('event_image_url', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('background_url', models.CharField(max_length=255)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.event')),
            ],
            options={
                'db_table': 'event_data',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='organization_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='organization', to='api_rest.organization'),
        ),
        migrations.AddField(
            model_name='event',
            name='user_id',
            field=models.ManyToManyField(db_table='user_event', related_name='events', to='api_rest.UserE'),
        ),
        migrations.CreateModel(
            name='Associate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=255)),
                ('logo_url', models.CharField(max_length=255)),
                ('relevance', models.BooleanField(default=False)),
                ('event_id', models.ManyToManyField(db_table='event_associate', related_name='associates', to='api_rest.Event')),
            ],
            options={
                'db_table': 'associate',
            },
        ),
    ]
