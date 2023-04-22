from pyexpat import model
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class StudyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLevel
        fields = '__all__'

class StudyFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyFormat
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'

class StudyGroupSerializer(serializers.ModelSerializer):
    study_level = StudyLevelSerializer()
    course = CourseSerializer()

    class Meta:
        model = StudyGroup
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type = RoomTypeSerializer()

    class Meta:
        model = Room
        fields = '__all__'

class DepartmentBoardSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Department
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    last_login = serializers.CharField(source='user.last_login', required=False)
    date_joined = serializers.DateTimeField(source='user.date_joined')
    role = serializers.CharField(source='role.name')
    position = serializers.CharField(source='position.name')
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'middle_name',
                  'phone', 'email', 'show_conts', 'role', 'avatar',
                  'from_another_uni', 'teacher_schedule', 'position',
                  'last_login', 'date_joined']

class PersonSerializer(serializers.ModelSerializer):
    email = serializers.CharField(source='user.email')
    last_login = serializers.CharField(source='user.last_login', required=False)
    date_joined = serializers.DateTimeField(source='user.date_joined')
    role = serializers.CharField(source='role.name')
    study_group = serializers.CharField(source='study_group.name',required=False)
    specialization = serializers.CharField(source='specialization.name', required=False)
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'middle_name', 'specialization',
                  'phone', 'email', 'show_conts', 'role', 'study_group',
                  'avatar', 'last_login', 'date_joined']

class LinkSerializer(serializers.ModelSerializer):
    teacher = PersonSerializer()
    subject = SubjectSerializer()

    class Meta:
        model = Link
        fields = '__all__'

class StudyDaySerializer(serializers.ModelSerializer):
    study_group = serializers.CharField()
    lesson = LessonSerializer()
    subject = serializers.CharField()
    teacher = serializers.CharField()
    room = serializers.CharField()
    study_format = serializers.CharField(required=False)
    day_number = serializers.CharField(source="get_day_number_display")

    class Meta:
        model = StudyDay
        fields = '__all__'

class StudyDayCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDay
        fields = '__all__'