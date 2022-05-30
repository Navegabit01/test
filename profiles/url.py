from profiles import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'friend', views.FriendView, basename='Friends')
router.register(r'profile', views.ProfileView, basename='Profiles')