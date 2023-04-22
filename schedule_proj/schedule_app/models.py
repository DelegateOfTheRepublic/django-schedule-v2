from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.http import QueryDict
from django.utils.translation import gettext_lazy as _
from .utils import *

"""
Без изменений: тип аудитории, курс, кафедра, факультет, должность, роли,
               форма обучения(сейчас называется, как учебный формат), уровень высшего образования и дисциплины
"""

class StudyLevel(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class StudyForm(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Course(models.Model):
    number = models.IntegerField(max_length=1)

    def __str__(self) -> str:
        return f'{self.number} курс'

class StudyGroup(models.Model):
    name = models.CharField(max_length=128)
    study_level = models.ForeignKey(StudyLevel, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    email = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self) -> str:
        return self.short_name

class RoomType(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.name

class Room(models.Model):
    number = models.CharField(max_length=10)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.number

class DepartmentBoard(models.Model):
    name = models.CharField(max_length=256)
    number = models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Specialization(models.Model):
    name = models.CharField(max_length=256)
    short_name = models.CharField(max_length=32, blank=True, null=True)
    code = models.CharField(max_length=16)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    phone = models.CharField(max_length=12)
    avatar = models.ImageField(_("Image"), upload_to=create_user_data_path)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.last_name} {self.first_name[0]}. {self.middle_name[0]}.'

class Student(Person):
    show_conts = models.CharField(max_length=16, default='1, 1')
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.SET_NULL, null=True)

class Teacher(Person):
    show_conts = models.CharField(max_length=16, default='1, 1')
    from_another_uni = models.BooleanField(default=False)
    teacher_schedule = models.FileField(upload_to=create_user_data_path, validators=[FileExtensionValidator(allowed_extensions=["json"])], blank=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)

class Link(models.Model):
    AVAILABLE_PLATFORMS = [
        ('tg', 'Телеграмм'),
        ('wapp', 'What\'s app'),
        ('discord', 'Discord'),
        ('vk', 'ВКонтакте')
    ]

    title = models.CharField(max_length=256)
    platform_name = models.CharField(choices=AVAILABLE_PLATFORMS, max_length=64)
    link = models.CharField(max_length=512)
    icon = models.ImageField(upload_to='platform_icons/', blank=True, default=f'platforms_icons/{platform_name}')
    meeting_ident = models.CharField(max_length=32, blank=True, null=True)
    passcode = models.CharField(max_length=16, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_temp = models.BooleanField(default=False)
    meeting_temp_time = models.IntegerField(blank=True)

    def __str__(self) -> str:
        return self.platform_name

class GroupSocialLink(models.Model):
    study_group = models.ForeignKey(StudyGroup, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    link = models.ForeignKey(Link, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.link.platform_name}: {self.subject}'

class Template(models.Model):
    title = models.CharField(max_length=128)
    folder_name = models.CharField(max_length=128, blank=True)
    template_file = models.FileField(upload_to=templates)

    def __str__(self) -> str:
        return self.title

class StatusType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name

class Lesson(models.Model):
    is_fractional = models.BooleanField(default=False)
    is_top_week = models.BooleanField(default=False)
    actual_dates = models.CharField(max_length=256, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    study_group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    study_form = models.ForeignKey(StudyForm, on_delete=models.CASCADE, default=0, null=True)
    links = models.CharField(max_length=8, blank=True, null=True)

    def __str__(self) -> str:
        return self.subject

class LessonTimes(models.Model):
    ordinal_number = models.IntegerField(max_length=1)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self) -> str:
        return f'{self.ordinal_number} пара'

class LessonStatuses(models.Model):
    status_type = models.ForeignKey(StatusType, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    lesson_swaped_to = models.ForeignKey(Lesson, on_delete=models.CASCADE, blank=True, null=True, related_name='swaped_to')
    reason = models.TextField()
    time_shifted_to = models.IntegerField(blank=True, null=True)
    room_changed_to = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)
    has_homework = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.status_type

class StudyDay(models.Model):
    DAY_NUMBERS = [
        ("0", "Понедельник"),
        ("1", "Вторник"),
        ("2", "Среда"),
        ("3", "Четверг"),
        ("4", "Пятница"),
        ("5", "Суббота")
    ]

    day_number = models.CharField(choices=DAY_NUMBERS, max_length=1)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.DAY_NUMBERS[int(self.day_number)][1]}. Группа {self.lesson.study_group}. {self.lesson}'

    """@classmethod
    def get_group_st_days(self, st_group_name: str, specialization:str=None, course:str=None) -> QueryDict:
        if specialization and course:
            st_group_id = Person.objects.values('study_group__id').filter(specialization=specialization, study_group__course_id=course, study_group=st_group_name).first()
            st_group_id = st_group_id.get('study_group__id') if st_group_id else None
            return StudyDay.objects.filter(study_group__id=st_group_id,).order_by('lesson')
        return StudyDay.objects.filter(study_group=st_group_name).order_by('lesson') or StudyDay.objects.filter(study_group__name=st_group_name).order_by('lesson')"""