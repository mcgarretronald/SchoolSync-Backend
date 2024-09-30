from rest_framework import generics
from admin_user.models import Admin_user
from api.serializer import AdminUserSerializer

# List all admins and create new admin
class AdminUserListCreateView(generics.ListCreateAPIView):
    queryset = Admin_user.objects.all()
    serializer_class = AdminUserSerializer
