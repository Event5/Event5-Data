from django.shortcuts import render

from .models import UserE, Organization, Event, Schedule, Speaker, Registry, Associate, EventData
from .serializers import UserESerializer, EventSerializer, OrganizationSerializer, ScheduleSerializer, SpeakerSerializer, EventDataSerializer, RegistrySerializer, AssociateSerializer, OrganizerSerializer, EventOrganizerSerializer, DashboardAdminSerializer,  ScheduleSpeakerSerializer, CompleteEventSerializer

from rest_framework import status, generics
import django_filters.rest_framework

from rest_framework.views import APIView 
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status, generics

# User
class UserList(APIView):

    def get(self, request, format=None):
       user = UserE.objects.all()
       serializer = UserESerializer(user, many=True)
       return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserESerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    
    def get_object(self, email):
        try:
            return UserE.objects.get(email=email)
        except UserE.DoesNotExist:
            raise Http404
    
    def get(self, request, email, format=None):
        user = self.get_object(email)
        serializer = UserESerializer(user)
        return Response(serializer.data)
    
    def put(self, request, email, format=None):
        user = self.get_object(email)
        serializer = UserESerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email):
        user = self.get_object(email)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserDetailByID(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserE.objects.all()
    serializer_class = UserESerializer

# Events
class EventList(APIView):  
    
    def get(self, request, format=None):
       event = Event.objects.all()
       serializer = EventSerializer(event, many=True)
       return Response(serializer.data)


    def post(self, request, format=None):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventListUser(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('users', None)
        return self.queryset.filter(users=value)
     
class EventListOrganization(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('organization_id', None)
        return self.queryset.filter(organization_id_id=value)

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# Organization
class OrganizationList(APIView):

    def post(self, request, format=None):
        serializer = OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrganizationListUser(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('user_id', None)
        return self.queryset.filter(user_id=value)


class OrganizationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


# Schedule
class ScheduleList(APIView):

    def post(self, request, format=None):
        serializer = ScheduleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScheduleListEvent(generics.ListAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('event_id', None)
        return self.queryset.filter(event_id=value)


class ScheduleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer


# Speaker
class SpeakerList(APIView):

    def post(self, request, format=None):
        serializer = SpeakerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SpeakerListSchedule(generics.ListAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('schedule_id', None)
        return self.queryset.filter(schedule_id=value)


class SpeakerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer


# Event Data
class EventDataList(APIView):

    def post(self, request, format=None):
        serializer = EventDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EventDataListEvent(generics.ListAPIView):
    queryset = EventData.objects.all()
    serializer_class = EventDataSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('event_id', None)
        return self.queryset.filter(event_id=value)


class EventDataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventData.objects.all()
    serializer_class = EventDataSerializer


# Registry
class RegistryList(APIView):

    def post(self, request, format=None):
        serializer = RegistrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegistryListEvent(generics.ListAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('event_id', None)
        return self.queryset.filter(event_id=value)


class RegistryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer


# Associate
class AssociateList(APIView):
    
    def get(self, request, format=None):
       associate = Associate.objects.all()
       serializer = AssociateSerializer(associate, many=True)
       return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssociateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AssociateListEvent(generics.ListAPIView):
    queryset = Associate.objects.all()
    serializer_class = AssociateSerializer

    def get_queryset(self, *arg, **kwargs):
        value = self.request.query_params.get('event_id', None)
        return self.queryset.filter(event_id=value)


class AssociateDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Associate.objects.all()
    serializer_class = AssociateSerializer


# Dashboard

class EventOrganizerDetailByUserID(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventOrganizerSerializer

    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('users', None)
        return self.queryset.filter(users=value)

class EventOrganizerDetailByUrl(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventOrganizerSerializer

    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('url', None)
        return self.queryset.filter(url=value)

class DashboardAdminByUrl(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = DashboardAdminSerializer

    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('url', None)
        return self.queryset.filter(url=value)


class DashboardAdminByID(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = DashboardAdminSerializer

    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('users', None)
        return self.queryset.filter(user_id=value)


class CompleteEventByUrl(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = CompleteEventSerializer

    def get_queryset(self, *arg, **kwarg):
        value = self.request.query_params.get('url', None)
        return self.queryset.filter(url=value)


class CompleteEventByID(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = CompleteEventSerializer


class Organizer(APIView):
    
    def get(self, request, format=None):
       associate = UserE.objects.all()
       serializer = OrganizerSerializer(associate, many=True)
       return Response(serializer.data)
