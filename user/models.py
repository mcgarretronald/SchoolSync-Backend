# user/models.py

from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from subject.models import Subject

class BaseUser(AbstractUser):
    # Common fields
    gender = models.CharField(max_length=10, choices=[("Male", "Male"), ("Female", "Female"), ("Other", "Other")], null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    age = models.CharField(max_length=15, null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile_images/", null=True, blank=True)
    bg_profile_image = models.ImageField(upload_to="bg_profile_images/", null=True, blank=True)

    class Meta:
        abstract = True

    groups = models.ManyToManyField(
        Group,
        related_name='%(class)s_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_query_name='%(class)s_group'
    )
    
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='%(class)s_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='%(class)s_user_permission'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

# Admin inherits from BaseUser
class AdminUser(BaseUser):
    title = models.CharField(max_length=50, default="Administrator")

    class Meta:
        verbose_name = _("Admin User")
        verbose_name_plural = _("Admin Users")
        permissions = [
            ("can_view_all_admins", "Can view all admin users"),
            ("can_add_teacher", "Can add teachers"),
            ("can_add_student", "Can add students"),
            ("can_view_all_teachers", "Can view all teachers"),
            ("can_view_all_students", "Can view all students"),
            ("can_create_announcements", "Can create announcements"),
            ("can_delete_announcements", "Can delete announcements"),
        ]

# Teacher inherits from BaseUser
class TeacherUser(BaseUser):
    subjects = models.ManyToManyField('subject.Subject', related_name='taught_by', blank=True)
    title = models.CharField(max_length=50, default="Teacher")

    class Meta:
        verbose_name = _("Teacher User")
        verbose_name_plural = _("Teacher Users")
        permissions = [
            ("can_view_all_teachers", "Can view all teacher users"),
            ("can_add_student_grades", "Can add student grades"),
            ("can_create_announcements", "Can create announcements"),
            ("can_delete_announcements", "Can delete announcements"),
            ("can_view_all_students", "Can view all students"),
        ]

# Student inherits from BaseUser
class StudentUser(BaseUser):
    subjects = models.ManyToManyField(Subject, related_name='students', blank=True)
    form = models.CharField(max_length=10, choices=[("One", "One"), ("Two", "Two"), ("Three", "Three"), ("Four", "Four")], null=True, blank=True)
    stream = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        verbose_name = _("Student User")
        verbose_name_plural = _("Student Users")
        permissions = [
            ("can_view_all_students", "Can view all student users"),
        ]

class ParentUser(BaseUser):
    relationship = models.CharField(max_length=50, null=True, blank=True)
    children = models.ManyToManyField(StudentUser, related_name="parents", blank=True)

    class Meta:
        verbose_name = "Parent User"
        verbose_name_plural = "Parent Users"
        permissions = [
            ("can_view_all_parents", "Can view all parent users"),
            ("can_send_emails_to_parents", "Can send emails to parents"),
        ]
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number} {self.email}"
