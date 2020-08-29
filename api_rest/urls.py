from django.urls import path, re_path
from api_rest import views

urlpatterns = [
    # User
    path('user/', views.UserList.as_view()),
    path('user/<email>', views.UserDetail.as_view()),
    path('user/id/<int:pk>', views.UserDetailByID.as_view()),
    # Event
    path('event/', views.EventList.as_view()),
    re_path(r'^event-user/$', views.EventListUser.as_view()),
    re_path(r'^event-organization/$', views.EventListOrganization.as_view()),
    path('event-detail/<int:pk>', views.EventDetail.as_view()),
    # Organization
    path('organization/', views.OrganizationList.as_view()),
    re_path(r'^organization-user/$', views.OrganizationListUser.as_view()),
    path('organization-detail/<int:pk>', views.OrganizationDetail.as_view()),
    
    # Schedule
    path('schedule/', views.ScheduleList.as_view()),
    re_path(r'^schedule-event/$', views.ScheduleListEvent.as_view()),
    path('schedule-detail/<int:pk>', views.ScheduleDetail.as_view()),
    # Speaker
    path('speaker/', views.SpeakerList.as_view()),
    re_path(r'^speaker-schedule/$', views.SpeakerListSchedule.as_view()),
    path('speaker-detail/<int:pk>', views.SpeakerDetail.as_view()),
    #  Event Data
    path('event-data/', views.EventDataList.as_view()),
    re_path(r'^event-data-event/$', views.EventDataListEvent.as_view()),
    path('event-data-detail/<int:pk>', views.EventDataDetail.as_view()),
    #  Registry
    path('registry/', views.RegistryList.as_view()),
    re_path(r'^registry-event/$', views.RegistryListEvent.as_view()),
    path('registry-detail/<int:pk>', views.RegistryDetail.as_view()),
    #  Associate
    path('associate/', views.AssociateList.as_view()),
    re_path(r'^associate-event/$', views.AssociateListEvent.as_view()),
    path('associate-detail/<int:pk>', views.AssociateDetail.as_view()),
    # Dashboard
    re_path(r'^event-organizer-id/$', views.EventOrganizerDetailByUserID.as_view()),
    re_path(r'^event-organizer-url/$', views.EventOrganizerDetailByUrl.as_view()),
    re_path(r'^dashboard-admin-url/$', views.DashboardAdminByUrl.as_view()),
    re_path(r'^dashboard-admin-id/$', views.DashboardAdminByID.as_view()),
    re_path(r'^complete-event-url/$', views.CompleteEventByUrl.as_view()),
    path('complete-event-id/<int:pk>', views.CompleteEventByID.as_view()),
    path('organaizer/', views.Organizer.as_view())
]
