from django.urls import path
from .views import AdminUserListCreateView

urlpatterns = [
    path('admins/', AdminUserListCreateView.as_view(), name='admin-list-create'),
]
