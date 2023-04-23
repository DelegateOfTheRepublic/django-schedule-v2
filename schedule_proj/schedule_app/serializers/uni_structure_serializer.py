from rest_framework import serializers
from schedule_app.models import Department, DepartmentBoard, Room, RoomType

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DepartmentBoardSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(source='department', queryset=Department.objects.all(), write_only=True)

    class Meta:
        model = DepartmentBoard
        fields = '__all__'

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    room_type_id = serializers.PrimaryKeyRelatedField(source='room_type', queryset=RoomType.objects.all(), write_only=True)
    room_type = RoomTypeSerializer(read_only=True)
    department = DepartmentSerializer(read_only=True)
    class Meta:
        model = Room
        fields = '__all__'