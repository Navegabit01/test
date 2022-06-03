from profiles import views
from rest_framework import routers
from django.urls import path


router = routers.DefaultRouter()
router.register(r'friends', views.FriendsView, basename='Friends')
router.register(r'profile', views.ProfileView, basename='Profile')


profile_patterns = [
    path(
        r"friends/profile/<int:profile_id>/",
        views.FriendsView.as_view({'get': 'profile_friends'}),
        name="friends_profile"
    ),
    path(
        r"friends/profile/<int:profile_id_1>/<int:profile_id_2>/",
        views.FriendsView.as_view({'get': 'graph_shorter_ways'}),
        name="friends_profile_array"
    )
] + router.urls
