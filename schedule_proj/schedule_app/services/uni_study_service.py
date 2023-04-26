from typing import Dict, Iterable, List
from django.http import QueryDict
from schedule_app.models import StudyLevel, Course, StudyForm, Subject,\
                                StatusType, StudyGroup, Exam, Lesson,\
                                LessonTimes, LessonStatuses, StudyDay

class StudyLevelService:
    def get_all(self) -> Iterable[StudyLevel]:
        return StudyLevel.objects.all()

class CourseService:
    def get_all(self) -> Iterable[Course]:
        return Course.objects.all()

class StudyFormService:
    def get_all(self) -> Iterable[StudyForm]:
        return StudyForm.objects.all()

class SubjectService:
    def get_all(self) -> Iterable[Subject]:
        return Subject.objects.all()

class StatusTypeService:
    def get_all(self) -> Iterable[StatusType]:
        return StatusType.objects.all()

class LessonTimesService:
    def get_all(self) -> Iterable[LessonTimes]:
        return LessonTimes.objects.all()

class StudyGroupService:
    def get_all(self) -> Iterable[StudyGroup]:
        return StudyGroup.objects.all()

    def get_one(self, pk:int) -> StudyGroup | None:
        return StudyGroup.objects.filter(pk=pk).first()

    def create(self, validate_data: Dict) -> StudyGroup:
        return StudyGroup.objects.create(**validate_data)

    def update(self, instance: StudyGroup, validate_data: Dict) -> int:
        return StudyGroup.objects.filter(pk=instance.pk).update(**validate_data)


class LessonStatusesService:
    def get_all(self) -> Iterable[LessonStatuses]:
        return LessonStatuses.objects.all()

    def get_one(self, pk:int) -> LessonStatuses | None:
        return LessonStatuses.objects.filter(pk=pk).first()

    def create(self, validate_data: Dict) -> LessonStatuses:
        return LessonStatuses.objects.create(**validate_data)

    def update(self, instance: LessonStatuses, validate_data: Dict) -> int:
        return LessonStatuses.objects.filter(pk=instance.pk).update(**validate_data)

class LessonService:
    def get_all(self) -> Iterable[Lesson]:
        return Lesson.objects.all()

    def get_one(self, pk: int) -> Lesson | None:
        return Lesson.objects.filter(pk=pk).first()

    def create(self, validate_data: Dict) -> Lesson:
        return Lesson.objects.create(**validate_data)

    def update(self, instance: Lesson, validate_data: Dict) -> int:
        return Lesson.objects.filter(pk=instance.pk).update(**validate_data)

class StudyDayService:
    def get_all(self) -> Iterable[StudyDay]:
        return StudyDay.objects.all()

    def get_one(self, pk: int) -> StudyDay | None:
        return StudyDay.objects.filter(pk=pk).first()

    def create(self, validate_data: Dict) -> StudyDay:
        return StudyDay.objects.create(**validate_data)

    def update(self, instance: StudyDay, validate_data: Dict) -> int:
        return StudyDay.objects.filter(pk=instance.pk).update(**validate_data)

class ExamService:
    def get_all(self) -> Iterable[Exam]:
        return Exam.objects.all()

    def get_one(self, pk: int) -> Exam | None:
        return Exam.objects.filter(pk=pk).first()

    def create(self, validate_data: Dict) -> Exam:
        return Exam.objects.create(**validate_data)

    def update(self, instance: Exam, validate_data: Dict) -> int:
        return Exam.objects.filter(pk=instance.pk).update(**validate_data)