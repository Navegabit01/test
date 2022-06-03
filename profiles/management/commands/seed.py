import requests
import json

from django.core.management.base import BaseCommand
from profiles.models import Friends, Profile


def get_profile_data():
    url = "https://randomapi.com/api/fb414b0fd22015ea575e7aa118052775"
    response = requests.get(url)
    return response.json()


class Command(BaseCommand):
    """ New command to populate database"""
    def handle(self, *args, **options) -> None:
        try:
            data_profile = get_profile_data()
            print(data_profile['results'])
            #data.save()
        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))


