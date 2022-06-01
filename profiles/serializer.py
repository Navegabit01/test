from rest_framework import serializers
from .models import Profile, Friends


class SerializerFriends(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ['id', 'profile1', 'profile2']


class SerializerProfiles(serializers.ModelSerializer):
    Friends = SerializerFriends(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'img', 'first_name', 'last_name', 'phone', 'address', 'city', 'zipcode', 'available', 'Friends']
