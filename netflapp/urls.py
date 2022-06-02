from profile import Profile
from django.urls import path
from .views import Home, Profilelist

urlpatterns=[
    path('', Home.as_view()),
    path('profile/', Profile.as_view(), name='profile_list')
]

