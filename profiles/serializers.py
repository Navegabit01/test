from rest_framework import serializers
from .models import Profile, Friend


class SerializerFriend(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = '__all__'


class SerializerProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
