from django.shortcuts import render

from .models import UserE, Organization, Event, Schedule, ScheduleSpeakers, Speaker, Registry, Associate, EventData
from .serializers import UserESerializer, EventSerializer, OrganizationSerializer, ScheduleSerializer, ScheduleSpeakersSerializer, SpeakerSerializer, EventDataSerializer, RegistrySerializer, AssociateSerializer

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.views import APIView 
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status

"""
class UserList(generics.ListCreateAPIView):
    queryset = UserE.objects.all()
    serializer_class = UserESerializer
    filter_backend = [DjangoFilterBackend]
    filterset_fields = ['email']
"""


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
"""
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserE.objects.all()
    serializer_class = UserESerializer
    filter_backend = [DjangoFilterBackend]
    filterset_fields = ['email']

"""

class UserDetail(APIView):
    
    def get_object(self, request, email, format=None):
        try:
            return UserE.object.get(email=email)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, email, format=None):
        user = self.get_object(email)
        serializer = UserESerializer(user)
        return Response(serializer.data)
    
    def put(self, request, email, format=None):
        user = self.get_object(emaile)
        serializer = UserESerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, email):
        user = self.get_object(email)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

