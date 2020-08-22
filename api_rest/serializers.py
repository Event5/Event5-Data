from rest_framework import serializers
from .models import UserE, Organization, Event, Schedule, ScheduleSpeakers, Speaker, Registry, Associate, EventData

class UserESerializer(serializers.ModelSerializer):
    class Meta:
        model = UserE
        fields = [
            'id', 
            'username', 
            'password', 
            'type_user', 
            'email', 
            'user_status'
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
        ]

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
        ]

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = [
            'id',
            'description',
        ]

class ScheduleSpeakersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleSpeakers
        fields = [
            'date_time',
            'title',
            'description'
        ]

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = [
            'id',
            'name',
            'biography',
            'role',
            'twitter',
            'photo_url'
        ]

class EventDataSerializer(serializers.ModelSerializer):
    class Meta:
        models = EventData
        fields = [
            'id',
            'logo_url',
            'title',
            'header_url',
            'description',
            'background_url',
            'date_create'
        ]

class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        models = Registry
        fields = [
            'email'
        ]

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        models = Associate
        fields = [
            'name',
            'url',
            'logo_url'
        ]

