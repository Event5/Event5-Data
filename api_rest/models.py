from django.db import models
from django.db.models.signals import post_save, post_delete
# Create the models to the api rest.

class UserE(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    type_user = models.CharField(max_length=50)
    email = models.CharField(max_length=150, unique=True)
    user_status = models.CharField(max_length=10)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = "user"


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    url = models.CharField(max_length=255, unique=True)
    event_start_date = models.DateTimeField()
    template = models.IntegerField()
    users = models.ManyToManyField('UserE', related_name='users', db_table='user_event')
    organization_id = models.ForeignKey('Organization', related_name='organization_event', on_delete=models.CASCADE)
    published = models.BooleanField(default=False)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "event"

class Organization(models.Model):
    name = models.CharField(max_length=150)
    url = models.CharField(max_length=255, unique=True)
    user_id = models.ForeignKey('UserE', related_name='organizations', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "organization"


class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    event_id = models.ForeignKey('Event', related_name='schedule_event', on_delete=models.CASCADE)

    class Meta:
        db_table = "schedule"


class Speaker(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    role = models.CharField(max_length=50)
    twitter = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)
    schedule_id = models.ManyToManyField('Schedule', related_name='schedule_speaker', db_table='shedule_speaker')

    class Meta:
        db_table = "speaker"

class EventData(models.Model):
    logo_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    event_image_url = models.CharField(max_length=255)
    description = models.TextField()
    background_url = models.CharField(max_length=255)
    event_id = models.ForeignKey('Event', related_name='event_data', on_delete=models.CASCADE)

    class Meta:
        db_table = "event_data"

class Registry(models.Model):
    email = models.CharField(max_length=100)
    event_id = models.ManyToManyField('Event', related_name='registrys', db_table='event-registry')

    class Meta:
        db_table = "registry"


class Associate(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    relevance = models.BooleanField(default=False)
    event_id = models.ManyToManyField('Event', related_name='event_associates', db_table='event_associate')

    class Meta:
        db_table = "associate"


