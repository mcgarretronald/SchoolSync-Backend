from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from admin_user.models import Admin_user

class AdminUserAPITestCase(APITestCase):

    def setUp(self):
        # Create some initial data for the tests
        self.admin_user_data = {
            "firstname": "John",
            "lastname": "Doe",
            "email": "johndoe@example.com",
            "password": "password123",
            "phonenumber": "0722334455",
            "location": "Nairobi",
            "username": "johndoe",
            "title": "Principal",
        }

        # Create an admin user to test list functionality
        Admin_user.objects.create(**self.admin_user_data)

    def test_list_admin_users(self):
        # List admin users API test
        url = reverse('admin-list-create')  # url name as defined in your urls.py
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure there's one admin user initially

    def test_create_admin_user(self):
        # Create new admin user API test
        url = reverse('admin-list-create')
        new_admin_data = {
            "firstname": "Jane",
            "lastname": "Smith",
            "email": "janesmith@example.com",
            "password": "adminpass",
            "phonenumber": "0745123456",
            "location": "Mombasa",
            "username": "janesmith",
            "title": "Vice Principal",
            # Omit profile_picture and bg_profile_picture fields
        }
        
        response = self.client.post(url, data=new_admin_data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Admin_user.objects.count(), 2)  # Now, two admin users should exist in the DB
        self.assertEqual(response.data['firstname'], 'Jane')
        self.assertEqual(response.data['lastname'], 'Smith')
