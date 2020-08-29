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
            'users',
            'organization_id',
            'published'
        ]

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'url',
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
        model = EventData
        fields = [
            'id',
            'title',
            'event_image_url',
            'description',
            'background_url',
            'event_id'
        ]



class RegistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = [
            'id',
            'email',
            'event_id'
        ]

class AssociateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associate
        fields = [
            'id',
            'name',
            'url',
            'logo_url',
            'relevance',
            'event_id'
        ]

# Dashboard 
class FilterListSerializer(serializers.ListSerializer):
    
    def to_representation(self, data):
        data = data.filter(type_user='organizer')
        return super(FilterListSerializer, self).to_representation(data)



class OrganizerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserE
        list_serializer_class = FilterListSerializer
        fields = [
            'id',
            'username',
            'email',
            'type_user',
        ]

class EventOrganizerSerializer(serializers.ModelSerializer):
    users = OrganizerSerializer(many=True, read_only=True)
    event_data = EventDataSerializer(many=True, read_only=True)
    public = serializers.IntegerField(source='registrys.count', read_only=True)
    associates = serializers.IntegerField(source='event_associates.count', read_only=True)

    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'url',
            'event_start_date',
            'template',
            'organization_id',
            'published',
            'public',
            'associates',
            'users',
            'event_data'
        ] 

class DashboardAdminSerializer(serializers.ModelSerializer):
    organization_event = EventOrganizerSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = [
            'id',
            'name',
            'url',
            'user_id',
            'organization_event'
        ]

class ScheduleSpeakerSerializer(serializers.ModelSerializer):
    schedule_speaker = SpeakerSerializer(many=True, read_only=True)
    conferences = serializers.IntegerField(source='schedule_speaker.count', read_only=True)
    class Meta:
        model = Schedule
        fields = [
            'id',
            'title',
            'description',
            'date_time',
            'event_id',
            'conferences',
            'schedule_speaker'
        ]


class CompleteEventSerializer(serializers.ModelSerializer):
    event_data = EventDataSerializer(many=True, read_only=True)
    event_associates = AssociateSerializer(many=True, read_only=True)
    schedule_event = ScheduleSpeakerSerializer(many=True, read_only=True)
    public = serializers.IntegerField(source='registrys.count', read_only=True)
    associates = serializers.IntegerField(source='event_associates.count', read_only=True)
    
    class Meta:
        model = Event
        fields = [
            'id',
            'event_name',
            'url',
            'event_start_date',
            'template',
            'users',
            'organization_id',
            'associates',
            'public',
            'event_data',
            'event_associates',
            'schedule_event'
        ]


