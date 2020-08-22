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

class Event(models.Model):
    event_name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    event_start_date = models.DateTimeField()
    template = models.CharField(max_length=100)
    user_id = models.ManyToManyField('UserE', related_name='events')
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

class Organization(models.Model):
    name = models.CharField(max_length=150)
    user_id = models.ForeignKey('UserE', related_name='organization', on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

"""
class Organizer(models.Model):
    user_id = models.ForeignKey('User',on_delete=models.CASCADE)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
"""

class Schedule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # speaker
    # time
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    
class ScheduleSpeakers(models.Model):
    date_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    schedule_id = models.ForeignKey('Schedule', on_delete=models.CASCADE) 
    speaker_id = models.ForeignKey('Speaker', on_delete=models.CASCADE)

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    role = models.CharField(max_length=50)
    twitter = models.CharField(max_length=100)
    photo_url = models.CharField(max_length=255)

class EventData(models.Model):
    logo_url = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    header_url = models.CharField(max_length=255)
    description = models.TextField()
    background_url = models.CharField(max_length=255)
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)

"""
class EventRegistry(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    registry_id = models.ForeignKey('Registry', on_delete=models.CASCADE)
"""

class Registry(models.Model):
    email = models.CharField(max_length=100)
    event_id = models.ManyToManyField('Event', related_name='registrys')

"""
class EventAssociate(models.Model):
    event_id = models.ForeignKey('Event', on_delete=models.CASCADE)
    associates_id = models.ForeignKey('Associate', on_delete=models.CASCADE)
"""

class Associate(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    logo_url = models.CharField(max_length=255)
    event_id = models.ManyToManyField(
        'Event', 
        related_name='associates'
        )
