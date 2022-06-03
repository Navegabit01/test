from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase, APISimpleTestCase


class FriendsViewTest(APITestCase):

    def setUp(self) -> None:
        '''
        Function set data for the test
        :return: None
        '''
        self.reverse_friends_profile_url = reverse("friends_profile", args=[1])
        self.create_profile_url = reverse("Profile-list")
        self.create_friends_url = reverse("Friends-list")
        for x in range(1, 4):
            data = {
                "id": x,
                "first_name": "Luis Alberto"+str(x),
                "last_name": "Vidal Mesa"+str(x),
                "phone": "52362879",
                "address": "asdadss",
                "city": "asdsdssa",
                "zipcode": 1231,
                "available": True
            }
            self.client.post(self.create_profile_url, data, format('json'))
        for x in range(1, 3):
            data = {
                "profile1": x,
                "profile2": x+1
            }
            self.client.post(self.create_friends_url, data, format('json'))


    def test_create_function(self) -> None:
        '''
        Test for create function
        :return: None
        '''
        data = {
            "first_name": "Luis Alberto",
            "last_name": "Vidal Mesa",
            "phone": "52362879",
            "address": "asdadss",
            "city": "asdsdssa",
            "zipcode": 1231,
            "available": True
        }

        response_create = self.client.post(self.create_profile_url, data, format('json'))
        data_copy = data
        data_copy['zipcode'] = 'str'
        response_format_zip_bad = self.client.post(self.create_profile_url, data_copy, format('json'))
        data_copy = data
        data_copy['img'] = 'str'
        response_create_img_error = self.client.post(self.create_profile_url, data, format('json'))
        self.assertEqual(response_create.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_format_zip_bad.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_create_img_error.status_code, status.HTTP_400_BAD_REQUEST)

    def test_profile_friends_function(self) -> None:
        '''
        Function for testing known friends of a given profile
        :return:
        '''
        response = self.client.get(self.reverse_friends_profile_url, arg=[1])
        self.assertEqual(len(response.data), 1)


