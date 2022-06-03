from random import randint
from random import choice

import requests

from django.core.management.base import BaseCommand
from profiles.models import Profile, Friends


class Command(BaseCommand):
    """ New command to populate database"""

    def get_profile_data(self):
        url = "https://randomapi.com/api/fb414b0fd22015ea575e7aa118052775"
        response = requests.get(url)
        return response.json()

    def delete_object(self, object) -> None:
        object.delete()

    def generate_profiles(self, options) -> None:
        for x in range(1, int(options['profiles']) + 1):
            data_profile = self.get_profile_data()
            data = Profile(id=x, **dict(data_profile['results'][0]))
            data.save()

    def generate_friends(self) -> None:
        profiles = Profile.objects.all()
        sentences = [x.id for x in profiles]
        rand = randint(1, profiles.count())
        print(rand, sentences)
        for _ in range(1, rand):
            profile1 = choice(sentences)
            sentences.remove(profile1)
            profile2 = choice(sentences)
            friend = Friends(profile1=Profile.objects.get(pk=profile1), profile2=Profile.objects.get(pk=profile2))
            friend.save()

    def add_arguments(self, parser) -> None:
        parser.add_argument('--profiles', help="Amount of profiles to create")

    def handle(self, *args, **options) -> None:
        try:
            self.delete_object(Profile.objects.all())
            self.delete_object(Friends.objects.all())
            self.generate_profiles(options)
            self.generate_friends()
        except Exception as e:
            print("Command complete with errors: {}".format(str(e)))
