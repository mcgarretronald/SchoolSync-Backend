from django.urls import path
from api.views import (
    AdminUserListView,       # View to handle listing and creating Admin users
    TeacherUserListView,     # View to handle listing and creating Teacher users
    StudentUserListView,     # View to handle listing and creating Student users
    SubjectListView,         # View to handle listing and creating Subjects
    CustomTokenObtainPairView,
    AdminUserDetailView,
    TeacherUserDetailView,
    StudentUserDetailView,
    ParentDetailView,
    ParentListView
)

urlpatterns = [
    path('admins/', AdminUserListView.as_view(), name='admin-user-list'),       
    path('subjects/', SubjectListView.as_view(), name='subject-list'),           
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('admins/<int:pk>/', AdminUserDetailView.as_view(), name='admin-detail'),
    path('teachers/', TeacherUserListView.as_view(), name='teacher-list'),
    path('teachers/<int:pk>/', TeacherUserDetailView.as_view(), name='teacher-detail'),
    path('students/', StudentUserListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentUserDetailView.as_view(), name='student-detail'),
    path('parents/', ParentListView.as_view(), name='parent-list'),  # Adjusted path for listing parents
    path('parents/create/', ParentDetailView.as_view(), name='create-parent'),  # Created a new path for creating parents
]
