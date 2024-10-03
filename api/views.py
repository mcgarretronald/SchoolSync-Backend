from rest_framework import generics  # Importing generic views for handling requests
from rest_framework.permissions import AllowAny  # Allow any user to access the views
from user.models import AdminUser, TeacherUser, StudentUser, ParentUser  # Importing user models
from subject.models import Subject  # Importing the subject model
from rest_framework_simplejwt.views import TokenObtainPairView  # Importing the token view for authentication
from api.serializer import (  # Importing the necessary serializers
    CustomTokenObtainPairSerializer,
    SubjectSerializer,
    AdminUserSerializer,
    TeacherUserSerializer,
    ParentUserSerializer,
    StudentUserSerializer
)

# View to retrieve, update, or delete a specific Admin user
class AdminUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AdminUser.objects.all()  # Fetch all admin users
    serializer_class = AdminUserSerializer  # Use the AdminUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to retrieve, update, or delete a specific Teacher user
class TeacherUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TeacherUser.objects.all()  # Fetch all teacher users
    serializer_class = TeacherUserSerializer  # Use the TeacherUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to list all Parent users and create a new Parent user
# In api/views.py

# In api/views.py

class ParentListView(generics.ListCreateAPIView):
    queryset = ParentUser.objects.all()
    serializer_class = ParentUserSerializer
    permission_classes = [AllowAny]  # Change permissions as needed

# View to retrieve, update, or delete a specific Parent user
class ParentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ParentUser.objects.all()  # Fetch all parent users
    serializer_class = ParentUserSerializer  # Use the ParentUserSerializer for data representation

# View to retrieve, update, or delete a specific Student user
class StudentUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = StudentUser.objects.all()  # Fetch all student users
    serializer_class = StudentUserSerializer  # Use the StudentUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to list all Admin users and create a new Admin user
class AdminUserListView(generics.ListCreateAPIView):
    queryset = AdminUser.objects.all()  # Fetch all admin users
    serializer_class = AdminUserSerializer  # Use the AdminUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to list all Teacher users and create a new Teacher user
class TeacherUserListView(generics.ListCreateAPIView):
    queryset = TeacherUser.objects.all()  # Fetch all teacher users
    serializer_class = TeacherUserSerializer  # Use the TeacherUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to list all Student users and create a new Student user
class StudentUserListView(generics.ListCreateAPIView):
    queryset = StudentUser.objects.all()  # Fetch all student users
    serializer_class = StudentUserSerializer  # Use the StudentUserSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; change to IsAdmin for production

# View to list all Teacher users (available to all users)
class TeacherListView(generics.ListAPIView):
    queryset = TeacherUser.objects.all()  # Fetch all teacher users
    serializer_class = TeacherUserSerializer  # Use the TeacherUserSerializer for data representation
    permission_classes = [AllowAny]  # Allow all authenticated users to view

# View to list all Student users (accessible by all users)
class StudentListView(generics.ListAPIView):
    queryset = StudentUser.objects.all()  # Fetch all student users
    serializer_class = StudentUserSerializer  # Use the StudentUserSerializer for data representation
    permission_classes = [AllowAny]  # Allow all authenticated users to view

# View to list all Subjects and create a new Subject
class SubjectListView(generics.ListCreateAPIView):
    queryset = Subject.objects.all()  # Fetch all subjects
    serializer_class = SubjectSerializer  # Use the SubjectSerializer for data representation
    permission_classes = [AllowAny]  # Allowing access; adjust as needed

# Custom token view to handle user authentication
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer  # Use the custom serializer for token generation
