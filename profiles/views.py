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
    """
            Class Profile (Data of persons)
        """
    queryset = Profile.objects.all()
    serializer_class = SerializerProfiles
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', )
    search_fields = ['id']
    ordering_fields = '__all__'


class FriendsView(viewsets.ModelViewSet):
    """
            Class Friends (relations of persons)
        """
    queryset = Friends.objects.all()
    serializer_class = SerializerFriends
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ('id', 'profile1', 'profile2')
    search_fields = ['id', 'profile1__first_name', 'profile2__first_name']
    ordering_fields = '__all__'

    def create(self, request, **kwargs):
        """
                Function override of create with some restriction
                (No profile are his own friend or have the same friend more than once)
            """
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
                return Response(
                    status=status.HTTP_400_BAD_REQUEST,
                    error="This convination exist"
                )
            return super(FriendsView, self).create(request)
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                error=str(e)
            )

    def profile_friends(self, request, profile_id=None):
        """
            Return the friends of the Profile selected
            """
        try:
            data = Friends.objects.annotate(
                knows=Concat('profile1__first_name', Value(' knows '), 'profile2__first_name', output_file=CharField())
            ).filter(
                Q(profile1=profile_id) | Q(profile2=profile_id)
            ).values('knows')
            return Response([x['knows'] for x in data])
        except Exception as e:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                error=str(e)
            )

    def graph_shorter_ways(self, request, profile_id_1, profile_id_2):
        """
           Graph shortest ways between 2 profiles
           """
        try:
            friends = Friends.objects.all().values(
                'profile1__id',
                'profile2__id',
            )
            node1 = Profile.objects.filter(pk=profile_id_1).get()
            node2 = Profile.objects.filter(pk=profile_id_2).get()

            connections = [
                [
                    friend['profile1__id'],
                    friend['profile2__id']
                ] for friend in friends
            ]
            graph = Graph(connections)
            path = graph.best_path(
                (node1.id),
                (node2.id),
            )
            if path:
                return Response(path[1:len(path) - 1])
            else:
                return Response("Path not exist")
        except:
            Response(status=status.HTTP_400_BAD_REQUEST)

