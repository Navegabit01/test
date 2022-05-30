from django.db import models
from rest_framework import status
from rest_framework.response import Response


class Profile(models.Model):
    img = models.ImageField(upload_to="fotos")
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    address = models.TextField(max_length=4096, blank=True)
    city = models.CharField(max_length=30, blank=True)
    zipcode = models.IntegerField(default=0, blank=True)
    available = models.BooleanField(default=True)


class Friend(models.Model):
    profile1 = models.ForeignKey(Profile, related_name='profile1', on_delete=models.CASCADE)
    profile2 = models.ForeignKey(Profile, related_name='profile2', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.profile1 == self.profile2:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            super(Friend, self).save(*args, **kwargs)

    def __str__(self):
        return "{}-{}".format(self.profile1, self.profile2)
