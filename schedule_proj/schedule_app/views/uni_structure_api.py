from typing import List
from django.http import JsonResponse, HttpRequest, QueryDict
from django.urls import re_path
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.views import APIView
from schedule_app.services.uni_structure_service import DepartmentService, DepartmentBoardService, RoomService, RoomTypeService
from schedule_app.serializers.uni_structure_serializer import DepartmentSerializer, DepartmentBoardSerializer, RoomSerializer, RoomTypeSerializer

class DepartmentApi(APIView):
    def get(self, request) -> JsonResponse:
        service = DepartmentService()
        serializer = DepartmentSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class DepartmentBoardApi(APIView):
    def get(self, request) -> JsonResponse:
        service = DepartmentBoardService()
        service_data = None
        dep_board_id: int | None = request.GET.get('id', None)
        many: bool = False

        if dep_board_id:
            service_data = service.get_one(dep_board_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = DepartmentBoardSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = DepartmentBoardSerializer(data=request.data, many=isinstance(request.data, List))
        service = DepartmentBoardService()

        if serializer.is_valid():
            service.create_dep_board(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = DepartmentBoardService()
        dep_board = service.get_one(request.query_params.get('id'))
        serializer = DepartmentBoardSerializer(dep_board, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class RoomApi(APIView):
    def get(self, request) -> JsonResponse:
        service = RoomService()

        service_data = None
        room_id: int | None = request.GET.get('id', None)
        many: bool = False

        if room_id:
            service_data = service.get_one(room_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = RoomSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = RoomService()
        serializer = RoomSerializer(data=request.data, many=isinstance(request.data, List))

        if serializer.is_valid():
            service.create_room(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = RoomService()
        room = service.get_one(request.query_params.get('id'))
        serializer = RoomSerializer(room, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(room, serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class RoomTypeApi(APIView):
    def get(self, request) -> JsonResponse:
        service = RoomTypeService()
        serializer = RoomTypeSerializer(service.get_all(), many=True)

        return JsonResponse(serializer.data, safe=False)

    def patch(self, request) -> JsonResponse:
        service = RoomTypeService()
        room_type = service.get_one(request.query_params.get('id'))
        serializer = RoomTypeSerializer(room_type, data=request.data)

        if serializer.is_valid():
            service.update(room_type, serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

urls = [
    re_path(r'^departments/', DepartmentApi.as_view()),
    re_path(r'^dep_boards/', DepartmentBoardApi.as_view()),
    re_path(r'^dep_board/<id:int>', DepartmentBoardApi.as_view()),
    re_path(r'^rooms/', RoomApi.as_view()),
    re_path(r'^rooms/<id:int>', RoomApi.as_view()),
    re_path(r'^room_types/', RoomTypeApi.as_view()),
    re_path(r'^room_types/<id:int>', RoomTypeApi.as_view()),
]