from rest_framework import serializers
from admin_user.models import Admin_user

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_user
        fields = '__all__'
