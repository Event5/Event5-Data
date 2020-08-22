from django.urls import path, re_path
from apirest import views

urlpatterns = [
    path('user/', views.UserList.as_view()),
    re_path(r'user/$', views.UserDetail.as_view()),
]
