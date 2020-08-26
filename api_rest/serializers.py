from rest_framework import serializers
from .models import UserE, Organization, Event, Schedule, Speaker, Registry, Associate, EventData

class UserESerializer(serializers.ModelSerializer):
    class Meta:
        model = UserE
        fields = [
            'id', 
            'username', 
            'password', 
            'type_user', 
            'email', 
            'user_status',
            'date_create'
        ]

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'url',
            'event_start_date',
            'template',
            'user_id',
            'organization_id'
        ]

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'user_id'
        ]


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'title',
            'description',
            'date_time',
            'event_id'
        ]
"""
class ScheduleSpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSpeakers
        fields = [
            'date_time',
            'title',
            'description'
        ]
"""

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = [
            'id',
            'name',
            'biography',
            'role',
            'twitter',
            'photo_url',
            'schedule_id'
        ]

class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        models = EventData
        fields = [
            'id',
            'logo_url',
            'title',
            'event_image_url',
            'description',
            'background_url',
            'event_id'
        ]

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        models = Registry
        fields = [
            'id',
            'email',
            'event_id'
        ]

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        models = Associate
        fields = [
            'id',
            'name',
            'url',
            'logo_url',
            'relevance',
            'event_id'
        ]

