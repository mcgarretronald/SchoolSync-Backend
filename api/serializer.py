from rest_framework import serializers
from user.models import AdminUser, TeacherUser, StudentUser, ParentUser
from subject.models import Subject
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Base serializer for common fields in BaseUser
class BaseUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = None  # This is abstract and not directly used
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'gender',
            'phone_number', 'location', 'about', 'age', 'profile_image',
            'bg_profile_image', 'password'
        ]

    def create(self, validated_data):
        user_class = self.Meta.model  # Dynamically get the model
        user = user_class(**validated_data)
        user.set_password(validated_data['password'])  # Hash the password
        user.save()  # Save the user to the database
        return user

# Serializer for AdminUser
class AdminUserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        model = AdminUser
        fields = BaseUserSerializer.Meta.fields + ['title']  # Add title field for admin

# Serializer for individual teacher details
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherUser  # Model for teacher
        fields = BaseUserSerializer.Meta.fields + ['subjects']  # Add subjects field

# Updated Subject serializer
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'name',]  # Add more details about the subject

# Serializer for StudentUser with improved subject display
class StudentUserSerializer(BaseUserSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)  # Read-only detailed subject info
    subject_ids = serializers.ListField(  # Accept list of subject IDs when creating/updating
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )

    parents = serializers.SerializerMethodField()

    class Meta:
        model = StudentUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'gender',
            'phone_number', 'location', 'password', 'about', 'age', 'profile_image',
            'bg_profile_image', 'form', 'stream', 'subjects', 'subject_ids', 'parents',
        ]

    def get_parents(self, obj):
        # Get all parents associated with the student
        parents = obj.parents.all()
        return [
            {
                'name': f"{parent.first_name} {parent.last_name} (Parent)",
                'phone_number': parent.phone_number
            } for parent in parents
        ]

    def create(self, validated_data):
        subjects_data = validated_data.pop('subject_ids', [])
        student = super().create(validated_data)

        # Set the subjects for the student
        subjects = Subject.objects.filter(id__in=subjects_data)
        if len(subjects) != len(subjects_data):
            missing_subjects = set(subjects_data) - set(subjects.values_list('id', flat=True))
            raise serializers.ValidationError({"subject_ids": f"Subjects not found: {', '.join(map(str, missing_subjects))}"})
        student.subjects.set(subjects)
        return student

    def update(self, instance, validated_data):
        subjects_data = validated_data.pop('subject_ids', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if subjects_data is not None:
            subjects = Subject.objects.filter(id__in=subjects_data)
            if len(subjects) != len(subjects_data):
                missing_subjects = set(subjects_data) - set(subjects.values_list('id', flat=True))
                raise serializers.ValidationError({"subject_ids": f"Subjects not found: {', '.join(map(str, missing_subjects))}"})
            instance.subjects.set(subjects)

        instance.save()
        return instance

# Parent serializer
# In api/serializer.py

class ParentUserSerializer(serializers.ModelSerializer):
    children = serializers.PrimaryKeyRelatedField(many=True, queryset=StudentUser.objects.all(), required=False)

    class Meta:
        model = ParentUser
        fields = [
            'id', 'username', 'first_name', 'last_name', 'email', 'gender',
            'phone_number', 'location', 'password', 'about', 'age', 'profile_image',
            'bg_profile_image', 'children',  # Include the children field
        ]

    def create(self, validated_data):
        children_ids = validated_data.pop('children', [])
        parent = ParentUser.objects.create(**validated_data)

        # Set the children for this parent if provided
        if children_ids:
            parent.children.set(children_ids)  # Associate existing children
        return parent

    def update(self, instance, validated_data):
        children_ids = validated_data.pop('children', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if children_ids is not None:
            instance.children.set(children_ids)

        instance.save()
        return instance


# Serializer for TeacherUser with subjects
class TeacherUserSerializer(BaseUserSerializer):
    subjects = SubjectSerializer(many=True, read_only=True)
    subject_names = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    class Meta(BaseUserSerializer.Meta):
        model = TeacherUser
        fields = BaseUserSerializer.Meta.fields + ['title', 'subjects', 'subject_names']

    def create(self, validated_data):
        subject_names = validated_data.pop('subject_names', [])
        teacher = super().create(validated_data)

        subjects = Subject.objects.filter(name__in=subject_names)
        if len(subjects) != len(subject_names):
            missing_subjects = set(subject_names) - set(subjects.values_list('name', flat=True))
            raise serializers.ValidationError({"subject_names": f"Subjects not found: {', '.join(missing_subjects)}"})

        teacher.subjects.set(subjects)
        return teacher

    def update(self, instance, validated_data):
        subject_names = validated_data.pop('subject_names', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if subject_names is not None:
            subjects = Subject.objects.filter(name__in=subject_names)
            if len(subjects) != len(subject_names):
                missing_subjects = set(subject_names) - set(subjects.values_list('name', flat=True))
                raise serializers.ValidationError({"subject_names": f"Subjects not found: {', '.join(missing_subjects)}"})

            instance.subjects.set(subjects)

        instance.save()
        return instance

# Serializer for login using JWT
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['email'] = user.email
        token['gender'] = user.gender
        token['phone_number'] = user.phone_number
        token['location'] = user.location
        token['about'] = user.about
        token['age'] = user.age
        token['profile_image'] = user.profile_image.url if user.profile_image else None
        token['bg_profile_image'] = user.bg_profile_image.url if user.bg_profile_image else None

        return token
