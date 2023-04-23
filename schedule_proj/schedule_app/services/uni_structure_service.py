from typing import Dict, Iterable, List
from schedule_app.models import Department, DepartmentBoard, Room, RoomType
from django.http import QueryDict

class DepartmentService:
    def get_all(self) -> Iterable[Department]:
        return Department.objects.all()

class DepartmentBoardService:
    def get_all(self) -> Iterable[DepartmentBoard]:
        return DepartmentBoard.objects.all()

    def get_one(self, pk: int) -> DepartmentBoard:
        return DepartmentBoard.objects.filter(id=pk).first()

    def create_dep_board(self, validate_data) -> None:
        DepartmentBoard.objects.bulk_create([DepartmentBoard(**item) for item in validate_data])

    def update(self, validate_data) -> None:
        DepartmentBoard.objects.update(**validate_data)

class RoomService:
    def get_all(self) -> Iterable[Room]:
        return Room.objects.all()

    def get_one(self, pk:int) -> Room:
        return Room.objects.filter(id=pk).first()

    def create_room(self, validate_data: List[QueryDict] | Dict) -> None:
        if isinstance(validate_data, List):
            Room.objects.bulk_create([Room(**item) for item in validate_data])
        else:
            Room.objects.create(**validate_data)

    def update(self, instance, validate_data) -> None:
        Room.objects.filter(pk=instance.id).update(**validate_data)

class RoomTypeService:
    def get_all(self) -> Iterable[RoomType]:
        return RoomType.objects.all()

    def get_one(self, pk: int) -> RoomType:
        return RoomType.objects.filter(id=pk).first()

    def update(self, instance, validate_data) -> None:
        RoomType.objects.filter(pk=instance.id).update(**validate_data)