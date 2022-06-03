from django.db import models
from rest_framework import status
from rest_framework.response import Response


# Create your models here.
class Profile(models.Model):
    img = models.ImageField(upload_to="fotos", blank=True)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone = models.CharField(max_length=20, blank=False)
    address = models.TextField(max_length=4096, blank=False)
    city = models.TextField(max_length=4096, blank=False)
    zipcode = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name


class Friends(models.Model):
    profile1 = models.ForeignKey(
        Profile,
        related_name="Profile1",
        on_delete=models.CASCADE,
    )
    profile2 = models.ForeignKey(
        Profile,
        related_name="Profile2",
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        if self.profile1 == self.profile2:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            super(Friends, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {}".format(self.profile1_id, self.profile2_id)
