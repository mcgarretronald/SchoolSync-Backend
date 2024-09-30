from django.db import models

# Create your models here.
class Admin_user (models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Ensure you use Django's password hashing method
    phonenumber = models.CharField(max_length=15)  # Use CharField for phone numbers
    location = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=50)
    profile_picture = models.ImageField(upload_to="profile_picture", null=True, blank=True)
    bg_profile_picture = models.ImageField(upload_to="bg_profile_picture", null=True, blank=True)
    
    def __str__ (self):
        return f"{self.firstname} {self.lastname} {self.email} {self.password} {self.phonenumber} {self.location} {self.username} {self.title}"