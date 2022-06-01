from profiles import views
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'friends', views.FriendsView, basename='Friends')
router.register(r'profile', views.ProfileView, basename='Profile')


profile_patterns = [
    path('friends/profile/', views.FriendsView.as_view({'get': 'profile'}))
                   ] + router.urls
