from django.test import TestCase

from rest_framework.test import  APIClient
from rest_framework import status

import json

from api_rest.models import UserE, Event, Schedule, Organization, Speaker, Registry, Associate, EventData

# user
class UserTestCase(TestCase):
    
    def setUp(self):
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )
    def test_post_user(self):
        client = APIClient()
        response = client.post(
            '/user/',
            {
                "id": 2,
                "username": "user 2",
                "password": "password",
                "type_user": "admin",
                "email": "user2@emailuser.com",
                "user_status": "activate"
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content), 
                        {
                        "id": 2,
                        "username": "user 2",
                        "password": "password",
                        "type_user": "admin",
                        "email": "user2@emailuser.com",
                        "user_status": "activate"})

    def test_user_get(self):
        client = APIClient()
        response = client.get('/user/user1@emailuser.com')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, {
            "id": 1,
            "username": "user 1",
            "password": "password",
            "type_user": "admin",
            "email": "user1@emailuser.com",
            "user_status": "activate"
        })
    
    def test_user_update(self):
        client = APIClient()
        test_user_update = {
             "id": 1,
             "username": "user",
             "password": "password",
             "type_user": "admin",
             "email": "user1@emailuser.com",
             "user_status": "activate"
         }
        response = client.put('/user/user1@emailuser.com', test_user_update)
        result =json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_user_update)

    def test_delete_user(self):
        client = APIClient()
        response = client.delete('/user/user1@emailuser.com')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = UserE.objects.filter(pk=1)
        self.assertFalse(user_exist)

# Organization
class OrganizationTestCase(TestCase):
    
    def setUp(self):
        
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )

        organization = Organization.objects.create(
            id=1,
            name = "user organization 1",
            url="/user-organization-1/",
            user_id = UserE.objects.get(id=1)
        )
    
    def test_post_organization(self):
        client = APIClient()
        response = client.post(
            '/organization/',
            {
                "id": 2,
                "name": "user organization 2",
                "url": "/user-organization-2/",
                "user_id": 1
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {
            "id": 2,
            "name": "user organization 2",
            "url": "/user-organization-2/",
            "user_id": 1
            })

    def test_get_organization_by_user(self):
        client = APIClient()
        response = client.get('/organization-user/?user_id=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        self.assertEqual(result,
        [{
            "id": 1,
            "name": "user organization 1",
            "url": "/user-organization-1/",
            "user_id": 1
        }])
     
    def test_organization_update(self):
        client = APIClient()
        test_organization_update = {
            "id": 1,
            "name": "organization 1",
            "url": "/user-organization-1/",
            "user_id": 1
        }
        response = client.put('/organization-detail/1', test_organization_update)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_organization_update)

    def test_delete_organizarion(self):

        organization = Organization.objects.create(
            id=3,
            name="user organization 3",
            url="/user-organization-3/",
            user_id=UserE.objects.get(id=1)
        )
        client = APIClient()
        response = client.delete('/organization-detail/3')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = Organization.objects.filter(pk=3)
        self.assertFalse(user_exist)
        
# Event
class EventTestCase(TestCase):

    def setUp(self):
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )

        organization = Organization.objects.create(
            id=1,
            name="user organization 1",
            url="/user-organization-1/",
            user_id=UserE.objects.get(id=1)
        )
        
        event = Event.objects.create(
            id = 1,
            event_name = "User event 1",
            url = "/user-event-1/",
            event_start_date = "2020-08-25T21:40:52Z",
            template = 1,
            organization_id = Organization.objects.get(id=1),
            published = True
        )

        event.users.add(user)
        
    def test_post_event(self):
        client = APIClient()
        response = client.post(
            '/event/',
            {
                "id": 2,
                "event_name": "User event 2",
                "url": "/user-event-2/",
                "event_start_date": "2020-08-25T21:40:52Z",
                "template": 2,
                "users": [1],
                "organization_id": 1,
                "published": True
            }
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {
                "id": 2,
                "event_name": "User event 2",
                "url": "/user-event-2/",
                "event_start_date": "2020-08-25T21:40:52Z",
                "template": 2,
                "users": [1],
                "organization_id": 1,
                "published": True
                })

    def test_event_by_organization_get(self):
        client = APIClient()
        response = client.get('/event-organization/?organization_id=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [{
            "id": 1,
            "event_name": "User event 1",
            "url": "/user-event-1/",
            "event_start_date": "2020-08-25T21:40:52Z",
            "template": 1,
            "users": [1],
            "organization_id": 1, 
            "published":True
        }])

    def test_event_by_user_get(self):
        client = APIClient()
        response = client.get('/event-user/?users=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [{
            "id": 1,
            "event_name": "User event 1",
            "url": "/user-event-1/",
            "event_start_date": "2020-08-25T21:40:52Z",
            "template": 1,
            "users": [1],
            "organization_id": 1,
            "published": True
        }])


    def test_event_update(self):
        client = APIClient()
        test_event_update = {
            "id": 1,
            "event_name": "event 1",
            "url": "/user-event-1/",
            "event_start_date": "2020-08-25T21:40:52Z",
            "template": 1,
            "users": [1],
            "organization_id": 1,
            "published": True
        }
        response = client.put('/event-detail/1', test_event_update)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_event_update)

    def test_delete_event(self):
        client = APIClient()
        response = client.delete('/event-detail/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = Event.objects.filter(pk=1)
        self.assertFalse(user_exist)

# Schedule
class ScheduleTestCase(TestCase):
    def setUp(self):
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )

        organization = Organization.objects.create(
            id=1,
            name="user organization 1",
            url="/user-organization-1/",
            user_id=UserE.objects.get(id=1)
        )

        event = Event.objects.create(
            id=1,
            event_name="User event 1",
            url="/user-event-1/",
            event_start_date="2020-08-25T21:40:52Z",
            template=1,
            organization_id=Organization.objects.get(id=1),
             published = True
        )
        event.users.add(user)

        schedule = Schedule.objects.create(
            id = 1,
            title = "schedule user event 1",
            description = "description user event 1",
            date_time = "2020-08-25T21:40:52Z",
            event_id = Event.objects.get(id=1)
        )

    def test_schedule_post(self):
        client = APIClient()
        response = client.post(
            '/schedule/',
            {
                "id": 2,
                "title": "schedule user event 1",
                "description": "description user event 1",
                "date_time": "2020-08-25T21:40:52Z",
                "event_id": 1
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {
            "id": 2,
            "title": "schedule user event 1",
            "description": "description user event 1",
            "date_time": "2020-08-25T21:40:52Z",
            "event_id": 1
        })

    def test_schedule_get(self):
        client = APIClient()
        response = client.get('/schedule-event/?event_id=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [{
            "id": 1,
            "title": "schedule user event 1",
            "description": "description user event 1",
            "date_time": "2020-08-25T21:40:52Z",
            "event_id": 1
        }])

    

    def test_schedule_update(self):
        client = APIClient()
        test_event_update = {
            "id": 1,
            "title": "schedule event 1",
            "description": "description user event 1",
            "date_time": "2020-08-25T21:40:52Z",
            "event_id": 1
        }
        response = client.put('/schedule-detail/1', test_event_update)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_event_update)

    def test_schedule_delete(self):
        client = APIClient()
        response = client.delete('/schedule-detail/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = Schedule.objects.filter(pk=1)
        self.assertFalse(user_exist)

# Speaker
class SpeakerTestCase(TestCase):
    def setUp(self):
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )

        organization = Organization.objects.create(
            id=1,
            name="user organization 1",
            url="/user-organization-1/",
            user_id=UserE.objects.get(id=1)
        )

        event = Event.objects.create(
            id=1,
            event_name="User event 1",
            url="/user-event-1/",
            event_start_date="2020-08-25T21:40:52Z",
            template=1,
            organization_id=Organization.objects.get(id=1),
             published = True
        )
        event.users.add(user)

        schedule = Schedule.objects.create(
            id = 1,
            title = "schedule user event 1",
            description = "description user event 1",
            date_time = "2020-08-25T21:40:52Z",
            event_id = Event.objects.get(id=1)
        )

        speaker = Speaker.objects.create(
            id = 1,
            name = "User 2",
            biography = "user 2 is a nice guy",
            role = "speaker",
            twitter = "@user2",
            photo_url = "/photo-url/",
        )

        speaker.schedule_id.add(schedule)

    def test_speaker_post(self):
        client = APIClient()
        response = client.post(
            '/speaker/',
            {
                "id": 2,
                "name": "User 3",
                "biography": "user 3 is a nice guy",
                "role": "speaker",
                "twitter": "@user3",
                "photo_url": "/photo-url/",
                "schedule_id": [1]
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {
            "id": 2,
            "name": "User 3",
            "biography": "user 3 is a nice guy",
            "role": "speaker",
            "twitter": "@user3",
            "photo_url": "/photo-url/",
            "schedule_id": [1]
        })

    def test_speaker_get(self):
        client = APIClient()
        response = client.get('/speaker-schedule/?schedule_id=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [{
            "id": 1,
            "name": "User 2",
            "biography": "user 2 is a nice guy",
            "role": "speaker",
            "twitter": "@user2",
            "photo_url": "/photo-url/",
            "schedule_id": [1]
        }])

    def test_speaker_update(self):
        client = APIClient()
        test_event_update = {
            "id": 1,
            "name": "User",
            "biography": "user is a nice guy",
            "role": "speaker",
            "twitter": "@user2",
            "photo_url": "/photo-url/",
            "schedule_id": [1]
        }
        response = client.put('/speaker-detail/1', test_event_update)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_event_update)

    def test_speaker_delete(self):
        client = APIClient()
        response = client.delete('/speaker-detail/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = Speaker.objects.filter(pk=1)
        self.assertFalse(user_exist)


# Event Data
class EventDataTestCase(TestCase):
    def setUp(self):
        user = UserE.objects.create(
            id=1,
            username="user 1",
            password="password",
            type_user="admin",
            email="user1@emailuser.com",
            user_status="activate"
        )

        organization = Organization.objects.create(
            id=1,
            name="user organization 1",
            url="/user-organization-1/",
            user_id=UserE.objects.get(id=1)
        )

        event = Event.objects.create(
            id=1,
            event_name="User event 1",
            url="/user-event-1/",
            event_start_date="2020-08-25T21:40:52Z",
            template=1,
            organization_id=Organization.objects.get(id=1),
            published=True
        )
        event.users.add(user)

        event_data = EventData.objects.create(
            id = 1,
            logo_url = "logo-url",
            title = "title event",
            event_image_url = "/event-image-url/",
            description = "description event",
            background_url = "/background-url/",
            event_id = Event.objects.get(id=1)
        )

    def test_event_data_post(self):
        client = APIClient()
        response = client.post(
            '/event-data/',
            {
            "id":2,
            "logo_url": "logo-url",
            "title": "title event 2",
            "event_image_url":"/event-image-url/",
            "description":"description event",
            "background_url":"/background-url/",
            "event_id":1
            }
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json.loads(response.content),
                         {
            "id": 2,
            "logo_url": "logo-url",
            "title": "title event 2",
            "event_image_url": "/event-image-url/",
            "description": "description event",
            "background_url": "/background-url/",
            "event_id": 1
        })

    def test_event_data_get(self):
        client = APIClient()
        response = client.get('/event-data-event/?event_id=1')
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, [{
            "id": 1,
            "logo_url": "logo-url",
            "title": "title event",
            "event_image_url": "/event-image-url/",
            "description": "description event",
            "background_url": "/background-url/",
            "event_id": 1
        }])

    def test_event_data_update(self):
        client = APIClient()
        test_event_update = {
            "id": 1,
            "logo_url": "logo-url",
            "title": "event",
            "event_image_url": "/event-image-url/",
            "description": "description full event",
            "background_url": "/background-url/",
            "event_id": 1
        }
        response = client.put('/event-data-detail/1', test_event_update)
        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, test_event_update)

    def test_event_data_delete(self):
        client = APIClient()
        response = client.delete('/event-data-detail/1')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        user_exist = Speaker.objects.filter(pk=1)
        self.assertFalse(user_exist)
