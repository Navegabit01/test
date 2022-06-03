import requests

from django.core.management.base import BaseCommand
from profiles.models import Friends, Profile


def get_profile_data():
    url = "https://randomapi.com/api/fb414b0fd22015ea575e7aa118052775"
    response = requests.get(url)
    return response.json()


class Command(BaseCommand):
    """ New command to populate database"""

    def add_arguments(self, parser):
        parser.add_argument('--profiles', help="Amount of profiles to create")

    def handle(self, *args, **options) -> None:
        try:
            Profile.objects.all().delete()
            for x in range(1, int(options['profiles'])+1):
                data_profile = get_profile_data()
                data = Profile(id=x, **dict(data_profile['results'][0]))
                data.save()
            print(Profile.objects.all().values())
        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))

