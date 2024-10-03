from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from user.models import AdminUser, TeacherUser, StudentUser, ParentUser

class UserApiTests(APITestCase):

    def setUp(self):
        # Create Admin User
        self.admin_user = AdminUser.objects.create_user(
            username='admin1',
            first_name='Admin',
            last_name='User',
            email='admin@example.com',
            password='adminpass',
            gender='Male',
            phone_number='1234567890'
        )

        # Create Teacher User
        self.teacher_user = TeacherUser.objects.create_user(
            username='teacher1',
            first_name='Teacher',
            last_name='User',
            email='teacher@example.com',
            password='teacherpass',
            gender='Female',
            phone_number='0987654321'
        )

        # Create Student User
        self.student_user = StudentUser.objects.create_user(
            username='student1',
            first_name='Student',
            last_name='User',
            email='student@example.com',
            password='studentpass',
            gender='Other',
            phone_number='1122334455',
            form='One',
            stream='A'
        )

        # Create Parent User
        self.parent_user = ParentUser.objects.create_user(
            username='parent1',
            first_name='Parent',
            last_name='User',
            email='parent@example.com',
            password='parentpass',
            gender='Female',
            phone_number='5566778899'
        )

    def test_create_admin_user(self):
        url = reverse('admin-user-list')
        data = {
            "username": "admin2",
            "first_name": "Admin2",
            "last_name": "User2",
            "email": "admin2@example.com",
            "password": "adminpass2",
            "gender": "Male",
            "phone_number": "1234567891"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AdminUser.objects.count(), 2)

    def test_create_teacher_user(self):
        url = reverse('teacher-list')
        data = {
            "username": "teacher2",
            "first_name": "Teacher2",
            "last_name": "User2",
            "email": "teacher2@example.com",
            "password": "teacherpass2",
            "gender": "Female",
            "phone_number": "0987654322"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TeacherUser.objects.count(), 2)

    def test_create_student_user(self):
        url = reverse('student-list')
        data = {
            "username": "student2",
            "first_name": "Student2",
            "last_name": "User2",
            "email": "student2@example.com",
            "password": "studentpass2",
            "gender": "Other",
            "phone_number": "1122334456",
            "form": "Two",
            "stream": "B"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StudentUser.objects.count(), 2)

    # def test_create_parent_user(self):
    #     url = reverse('create-parent')  # Adjusted path for creating parents
    #     data = {
    #         "username": "parent2",
    #         "first_name": "Parent2",
    #         "last_name": "User2",
    #         "email": "parent2@example.com",
    #         "password": "parentpass2",
    #         "gender": "Female",
    #         "phone_number": "5566778900"
    #     }
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(ParentUser.objects.count(), 2)

    def test_list_teacher_users(self):
        url = reverse('teacher-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Only one teacher created in setUp

    def test_update_student_user(self):
        url = reverse('student-detail', args=[self.student_user.id])
        data = {
            "username": "updated_student",
            "first_name": "Updated",
            "last_name": "User",
            "email": "updated_student@example.com",
            "password": "studentpass",  # Password should remain unchanged
            "gender": "Other",
            "phone_number": "1122334457",
            "form": "Three",
            "stream": "C"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.student_user.refresh_from_db()
        self.assertEqual(self.student_user.first_name, "Updated")
        self.assertEqual(self.student_user.form, "Three")

    # def test_delete_teacher_user(self):
    #     url = reverse('teacher-detail', args=[self.teacher_user.id])
    #     response = self.client.delete(url)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #     self.assertEqual(TeacherUser.objects.count(), 1)  # Ensure one teacher user is deleted
