from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework import status

from .serializers import SerializerFriend, SerializerProfile
from .models import Friend, Profile


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = SerializerProfile
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id', )
    search_fields = ['id']
    ordering_fields = '__all__'


class FriendView(viewsets.ModelViewSet):
    queryset = Friend.objects.all()
    serializer_class = SerializerFriend
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('id', 'profile1__first_name', 'profile2__first_name')
    search_fields = ['id']
    ordering_fields = '__all__'
