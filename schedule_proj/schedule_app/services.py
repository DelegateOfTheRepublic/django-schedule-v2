from typing import Dict, Iterable
from .models import *

class SCourse:
    @classmethod
    def get_all(self) -> Iterable[Course]:
        return Course.objects.all()

class SDepartment:
    @classmethod
    def get_all(self) -> Iterable[Department]:
        return Department.objects.all()

class SDepartmentBoard:
    @classmethod
    def get_all(self) -> Iterable[DepartmentBoard]:
        return DepartmentBoard.objects.all()

class SLesson:
    @classmethod
    def get_all(self) -> Iterable[Lesson]:
        return Lesson.objects.all()

    @classmethod
    def get_by_times(self, start_time: str, end_time:str) -> Lesson:
        return Lesson.objects.get(start_time=start_time, end_time=end_time)

class SLink:
    @classmethod
    def get_all(self) -> Iterable[Link]:
        return Link.objects.all()

class SPosition:
    @classmethod
    def get_all(self) -> Iterable[Position]:
        return Position.objects.all()

class SPerson:
    @classmethod
    def get_all(self) -> Dict[(str, Iterable[Person])]:
        teachers = Person.objects.filter(role__name='Преподаватель')
        anothers = Person.objects.all().exclude(role__name='Преподаватель')
        return {'teachers': teachers, 'anothers': anothers}

    @classmethod
    def get_person_by_id(self, id: int) -> Person:
        return Person.objects.get(pk=id)

    @classmethod
    def get_teachers(self) -> Iterable[Person]:
        return Person.objects.filter(role__name='Преподаватель')

    @classmethod
    def create_teacher(self, validated_data):
        user_email = validated_data.pop('user')['email']
        role_id = validated_data.pop('role')['name']
        position_id = validated_data.pop('position')['name']

        validated_data['user'] = User.objects.get(email=user_email)
        validated_data['role'] = Role.objects.get(pk=role_id)
        validated_data['position'] = Position.objects.get(pk=position_id)

        return Person.objects.create(**validated_data)

    @classmethod
    def create_person(self, validated_data):
        user_email = validated_data.pop('user')['email']
        role_id = validated_data.pop('role')['name']

        validated_data['user'] = User.objects.get(email=user_email)
        validated_data['role'] = Role.objects.get(pk=role_id)

        print(validated_data)

        return Person.objects.create(**validated_data)

    @classmethod
    def update_person(self, validated_data):
        return Person.objects.update(**validated_data)

class SRole:
    @classmethod
    def get_all(self) -> Iterable[Role]:
        return Role.objects.all()

class SRoomType:
    @classmethod
    def get_all(self) -> Iterable[RoomType]:
        return RoomType.objects.all()

class SRoom:
    @classmethod
    def get_all(self) -> Iterable[Room]:
        return Room.objects.all()

class SStudyLevel:
    @classmethod
    def get_all(self) -> Iterable[StudyLevel]:
        return StudyLevel.objects.all()

class SStudyGroup:
    @classmethod
    def get_all(self) -> Iterable[StudyGroup]:
        return StudyGroup.objects.all()

    def get_groups_by(specialization, course):
        tmp = Person.objects.values('study_group_id').filter(specialization=specialization, study_group__course=course)
        res = []

        for st_group in tmp:
            res.append(StudyGroup.objects.get(id=st_group.get('study_group_id')))

        return res

    @classmethod
    def get_by_name(self, study_group_name) -> int:
        return StudyGroup.objects.get(name=study_group_name).id

class SStudyFormat:
    @classmethod
    def get_all(self) -> Iterable[StudyFormat]:
        return StudyFormat.objects.all()

class SStudyDay:
    @classmethod
    def get_all(self) -> Iterable[StudyDay]:
        return StudyDay.objects.all()

    @classmethod
    def group_by_days(self, study_days):
        st_group_days = {}

        for st_day in study_days:
            tmp = st_group_days.get(st_day.day_number, st_group_days)
            if isinstance(tmp, dict):
                tmp[st_day.day_number] = [st_day]
            else:
                tmp.append(st_day)

        return st_group_days

    @classmethod
    def create_study_days(self, validate_data) -> None:

        for i in range(len(validate_data)):
            validate_data[i]['study_group'] = StudyGroup.objects.get(pk=validate_data[i]['study_group'])
            if validate_data[i]['study_format'] != None:
                validate_data[i]['study_format'] = StudyFormat.objects.get(pk=validate_data[i]['study_format'])
            validate_data[i]['subject'] = Subject.objects.get(pk=validate_data[i]['subject'])
            validate_data[i]['lesson'] = Lesson.objects.get(pk=validate_data[i]['lesson'])
            validate_data[i]['room'] = Room.objects.get(pk=validate_data[i]['room'])
            validate_data[i]['teacher'] = Person.objects.get(pk=validate_data[i]['teacher'])

        return StudyDay.objects.bulk_create([StudyDay(**item) for item in validate_data])

    def get_group_st_days(st_group_name:str, specialization:str = None, course:str=None) -> Iterable[StudyDay]:
        return StudyDay.get_group_st_days(st_group_name, specialization, course)

    @classmethod
    def get_day_number_by_name(self, day_name:str) -> int:
        return [day[0] for day in StudyDay.DAY_NUMBERS if day[1] == day_name][0]

class SSubject:
    @classmethod
    def get_all(self) -> Iterable[Subject]:
        return Subject.objects.all()

class SSpecialization:
    @classmethod
    def get_all(self) -> Iterable[Specialization]:
        return Specialization.objects.all()