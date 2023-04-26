from rest_framework import serializers
from schedule_app.models import Room, StudyLevel, Course, StudyForm, Subject,\
                                StatusType, StudyGroup, Exam, Lesson,\
                                LessonTimes, LessonStatuses, StudyDay, Teacher

class StudyLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyLevel
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudyFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyForm
        fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class StatusTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusType
        fields = '__all__'

class StudyGroupSerializer(serializers.ModelSerializer):
    study_level_id = serializers.PrimaryKeyRelatedField(source='study_level', queryset=StudyLevel.objects.all(), write_only=True)
    study_level = serializers.CharField(read_only=True)

    course_id = serializers.PrimaryKeyRelatedField(source='course', queryset=Course.objects.all(), write_only=True)
    course = serializers.CharField(read_only=True)

    class Meta:
        model = StudyGroup
        fields = '__all__'

class ExamSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(source='subject', queryset=Subject.objects.all(), write_only=True)
    subject = serializers.CharField(read_only=True)

    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), write_only=True)
    teacher = serializers.CharField(read_only=True)

    consult_room_id = serializers.PrimaryKeyRelatedField(source='consult_room', queryset=Room.objects.all(), write_only=True)
    consult_room = serializers.CharField(read_only=True)

    exam_room_id = serializers.PrimaryKeyRelatedField(source='exam_room', queryset=Room.objects.all(), write_only=True)
    exam_room = serializers.CharField(read_only=True)

    class Meta:
        model = Exam
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    subject_id = serializers.PrimaryKeyRelatedField(source='subject', queryset=Subject.objects.all(), write_only=True)
    subject = serializers.CharField(read_only=True)

    teacher_id = serializers.PrimaryKeyRelatedField(source='teacher', queryset=Teacher.objects.all(), write_only=True)
    teacher = serializers.CharField(read_only=True)

    study_group_id = serializers.PrimaryKeyRelatedField(source='study_group', queryset=StudyGroup.objects.all(), write_only=True)
    study_group = serializers.CharField(read_only=True)

    room_id = serializers.PrimaryKeyRelatedField(source='room', queryset=Room.objects.all(), write_only=True)
    room = serializers.CharField(read_only=True)

    study_form_id = serializers.PrimaryKeyRelatedField(source='study_from', queryset=StudyForm.objects.all(), write_only=True)
    study_form = serializers.CharField(read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

class LessonTimesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonTimes
        fields = '__all__'

class LessonStatusesSerializer(serializers.ModelSerializer):
    status_type_id = serializers.PrimaryKeyRelatedField(source='status_type', queryset=StatusType.objects.all(), write_only=True)
    status_type = serializers.CharField(read_only=True)

    lesson_id = serializers.PrimaryKeyRelatedField(source='lesson', queryset=Lesson.objects.all(), write_only=True)
    lesson = serializers.CharField(read_only=True)

    lesson_swaped_to_id = serializers.PrimaryKeyRelatedField(source='lesson_swaped_to', queryset=Lesson.objects.all(), write_only=True)
    lesson_swaped_to = serializers.CharField(read_only=True)

    room_changed_to_id = serializers.PrimaryKeyRelatedField(source='room_changed_to', queryset=Room.objects.all(), write_only=True)
    room_changed_to = serializers.CharField(read_only=True)

    class Meta:
        model = LessonStatuses
        fields = '__all__'

class StudyDaySerializer(serializers.ModelSerializer):
    lesson_id = serializers.PrimaryKeyRelatedField(source='lesson', queryset=Lesson.objects.all(), write_only=True)
    lesson = serializers.CharField(read_only=True)

    class Meta:
        model = StudyDay
        fields = '__all__'