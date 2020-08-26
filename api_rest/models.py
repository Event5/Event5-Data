from django.db import models

# Create the models to the api rest.

class UserE(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    type_user = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    user_status = models.CharField(max_length=10)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user"


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    event_start_date = models.DateTimeField()
    template = models.IntegerField()
    user_id = models.ManyToManyField('UserE', related_name='events', db_table='user_event')
    organization_id = models.ForeignKey('Organization', related_name='organization', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "event"

class Organization(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.ForeignKey('UserE', related_name='organizations', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "organization"


class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date_time = models.DateTimeField()
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        db_table = "schedule"

"""   
class ScheduleSpeakers(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    schedule_id = models.ForeignKey('Schedule', on_delete=models.CASCADE) 
"""

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    role = models.CharField(max_length=50)
    twitter = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)
    schedule_id = models.ManyToManyField('Schedule', related_name='Schedule', db_table='shedule_speaker')

    class Meta:
        db_table = "speaker"

class EventData(models.Model):
    logo_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    event_image_url = models.CharField(max_length=255)
    description = models.TextField()
    background_url = models.CharField(max_length=255)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

    class Meta:
        db_table = "event_data"

"""
class EventRegistry(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    registry_id = models.ForeignKey('Registry', on_delete=models.CASCADE)
"""

class Registry(models.Model):
    email = models.CharField(max_length=100)
    event_id = models.ManyToManyField('Event', related_name='registrys', db_table='event-registry')

    class Meta:
        db_table = "registry"

"""
class EventAssociate(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    associates_id = models.ForeignKey('Associate', on_delete=models.CASCADE)
"""

class Associate(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    relevance = models.BooleanField(default=False)
    event_id = models.ManyToManyField('Event', related_name='associates', db_table='event_associate')

    class Meta:
        db_table = "associate"
