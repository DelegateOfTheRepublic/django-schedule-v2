from typing import Dict, Iterable, List
from schedule_app.models import Person, Teacher, Student, Position, Specialization
from django.http import QueryDict
from django.contrib.auth.models import User

class UserService:
    @classmethod
    def create_user(self, validate_data: Dict, password: str) -> User | None:
        email: str = validate_data.pop('user').get('email')
        username: str = validate_data.get('first_name')
        new_user: User = User.objects.create(username=username, email=email)
        new_user.set_password(password)
        new_user.save()

        return new_user

    @classmethod
    def update_user(self, validate_data:Dict, instance: Person) -> int | None:
        email: str = validate_data.pop('user').get('email', instance.user.email)
        username: str = validate_data.get('first_name', instance.first_name)

        return User.objects.filter(pk=instance.user.id).update(email=email, username=username)

class PositionService:
    def get_all(self) -> Iterable[Position]:
        return Position.objects.all()

class SpecializationService:
    def get_all(self) -> Iterable[Specialization]:
        return Specialization.objects.all()

class StudentService:
    def get_all(self) -> Iterable[Student]:
        return Student.objects.all()

    def get_one(self, pk:int) -> Student | None:
        return Student.objects.filter(id=pk).first()

    def create_student(self, validate_data:Dict) -> Student | None:
        password: str = 'GeNeRaLPersonPwD@1'
        new_user: User = UserService.create_user(validate_data, password)

        return Student.objects.create(user=new_user, **validate_data)

    def update_student(self, instance:Student, validate_date:Dict) -> Student | None:
        email: str = validate_date.pop('user').get('email', instance.user.email)
        username: str = validate_date.get('first_name', instance.first_name)

        User.objects.filter(pk=instance.user.id).update(email=email, username=username)

        return Student.objects.filter(pk=instance.id).update(**validate_date)

class TeacherService:
    def get_all(self) -> Iterable[Teacher]:
        return Teacher.objects.all()

    def get_one(self, pk:int) -> Teacher | None:
        return Teacher.objects.filter(pk=pk).first()

    def create_teacher(self, validate_data:Dict) -> Teacher | None:
        password: str = 'GeNeRaLPersonPwD@2'
        new_user: User = UserService.create_user(validate_data, password)

        return Teacher.objects.create(user=new_user, **validate_data)

    def update_teacher(self, instance:Teacher, validate_data:Dict) -> Teacher | None:
        UserService.update_user(validate_data, instance)

        return Teacher.objects.filter(pk = instance.id).update(**validate_data)