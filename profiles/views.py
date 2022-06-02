from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework import status
from rest_framework.response import Response

from .serializer import SerializerProfiles, SerializerFriends
from .models import Profile, Friends


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = SerializerProfiles
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', )
    search_fields = ['id']
    ordering_fields = '__all__'


class FriendsView(viewsets.ModelViewSet):
    queryset = Friends.objects.all()
    serializer_class = SerializerFriends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'profile1', 'profile2')
    search_fields = ['id', 'profile1__first_name', 'profile2__first_name']
    ordering_fields = '__all__'

    def create(self, request):
        try:
            if request.data['profile1'] == request.data['profile2'] or Friends.objects.filter(
                    Q(profile1=request.data['profile1'], profile2=request.data['profile2'])) or Friends.objects.filter(
                             Q(profile1=request.data['profile2'], profile2=request.data['profile1'])):
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return super(FriendsView, self).create(request)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def profile(self, request):
        data = {
            "status": 0,
            "message": "Success",
            "data": {
                "updatedAt": "2020-08-31 17:49:15",
                "serverTime": "2022-03-23 15:10:11",
                "news": ['data', 'data1']
            }
        }
        return Response(data)

