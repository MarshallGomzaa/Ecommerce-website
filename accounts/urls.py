from django.urls import path
from .views import *
urlpatterns = [
    path('register/', user_registration, name='register'),
    path('login/', user_login, name='login'),
    path("logout/", user_logout, name="logout"),
    path("user_profile/", user_profile, name="user_profile"),
]
