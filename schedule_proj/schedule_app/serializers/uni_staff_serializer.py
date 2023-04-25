from rest_framework import serializers
from schedule_app.models import Person, StudyGroup, Teacher, Student, Position, Role, Specialization

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    department = serializers.CharField(read_only=True)
    class Meta:
        model = Specialization
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    role = serializers.CharField(source='role.name', read_only=True)
    role_id = serializers.PrimaryKeyRelatedField(source='role', queryset=Role.objects.all(), write_only=True)

    class Meta:
        model = Person
        exclude = ['user']

class TeacherSerializer(PersonSerializer):
    position = serializers.CharField(source='position.name', read_only=True)
    position_id = serializers.PrimaryKeyRelatedField(source='position', queryset=Position.objects.all(), write_only=True)
    class Meta:
        model = Teacher
        exclude = ['user']

class StudentSerializer(PersonSerializer):
    study_group = serializers.CharField(source='study_group.name', read_only=True)
    specialization = serializers.CharField(source='specialization.name', read_only=True)
    study_group_id = serializers.PrimaryKeyRelatedField(source='study_group', queryset=StudyGroup.objects.all(), write_only=True)
    specialization_id = serializers.PrimaryKeyRelatedField(source='specialization', queryset=Specialization.objects.all(), write_only=True)
    class Meta:
        model = Student
        exclude = ['user']