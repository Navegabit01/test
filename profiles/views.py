from .graph_class import Graph

from django.db.models import Q, Value, CharField
from django.db.models.functions import Concat
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
                    Q(
                        profile1=request.data['profile1'],
                        profile2=request.data['profile2'])
            ) or Friends.objects.filter(
                             Q(
                                 profile1=request.data['profile2'],
                                 profile2=request.data['profile1'])
            ):
                return Response(status=status.HTTP_400_BAD_REQUEST, error="This convination exist")
            return super(FriendsView, self).create(request)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, error=str(e))

    def profile_friends(self, request, profile_id=None):
        try:
            data = Friends.objects.annotate(
                knows=Concat('profile1__first_name', Value(' knows '), 'profile2__first_name', output_file=CharField())
            ).filter(
                Q(profile1=profile_id) | Q(profile2=profile_id)
            ).values('knows')
            return Response([x['knows'] for x in data])
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST, error=str(e))

    def graph_shorter_ways(self, request, profile_id_1, profile_id_2):
        friends = Friends.objects.all().values(
            'profile1__id',
            'profile1__first_name',
            'profile2__id',
            'profile2__first_name'
        )
        node1 = Profile.objects.filter(pk=profile_id_1).get()
        node2 = Profile.objects.filter(pk=profile_id_2).get()

        connections = [
                [
                    str(friend['profile1__first_name'])+"-"+str(friend['profile1__id']),
                    str(friend['profile2__first_name'])+'-'+str(friend['profile2__id'])
                ] for friend in friends
            ]
        graph = Graph(connections)
        path = graph.BFS_SP(
            (node1.first_name+'-'+str(node1.id)),
            (node2.first_name+'-'+str(node2.id)),
        )
        if path:
            return Response(path[1:len(path)-1])
        else:
            return Response("Path not exist")
