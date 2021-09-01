from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class FileTests(APITestCase):
    def setUp(self) -> None:
        user = get_user_model()
        self.test_user = user(username='test_user', password="qwerty123")
        self.test_user.save()

    def test_file_list_not_permissions(self):
        response = self.client.get(reverse('upload_file-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_file_list_permissions(self):
        self.client.force_authenticate(user=self.test_user)
        response = self.client.get(reverse('upload_file-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
