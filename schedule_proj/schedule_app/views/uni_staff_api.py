from typing import List
from django.http import JsonResponse, HttpRequest, QueryDict
from django.urls import re_path
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.views import APIView
from schedule_app.services.uni_staff_service import StudentService, TeacherService, PositionService, SpecializationService
from schedule_app.serializers.uni_staff_serializer import StudentSerializer, TeacherSerializer, PositionSerializer, SpecializationSerializer

class PositionApi(APIView):
    def get(self, request) -> JsonResponse:
        service = PositionService()
        serializer = PositionSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class SpecializationApi(APIView):
    def get(self, request) -> JsonResponse:
        service = SpecializationService()
        serializer = SpecializationSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudentApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StudentService()

        service_data = None
        student_id: int | None = request.GET.get('id', None)
        many: bool = False

        if student_id:
            service_data = service.get_one(student_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = StudentSerializer(service_data, many=many)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = StudentService()
        serializer = StudentSerializer(data=request.data, many=isinstance(request.data, List))

        if serializer.is_valid():
            service.create_student(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = StudentService()
        serializer = StudentSerializer(data=request.data, partial=True)
        student = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_student(student, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class TeacherApi(APIView):
    def get(self, request) -> JsonResponse:
        service = TeacherService()

        service_data = None
        teacher_id: int | None = request.GET.get('id', None)
        many: bool = False

        if teacher_id:
            service_data = service.get_one(teacher_id)
            if not service_data:
                return JsonResponse({'status': status.HTTP_204_NO_CONTENT})
        else:
            service_data = service.get_all()
            many = True

        serializer = TeacherSerializer(service_data, many=many)

        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = TeacherService()
        serializer = TeacherSerializer(data=request.data, many=isinstance(request.data, List))

        if serializer.is_valid():
            service.create_teacher(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = TeacherService()
        serializer = TeacherSerializer(data=request.data, partial=True)
        student = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_teacher(student, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

urls = [
    re_path(r'^students/', StudentApi.as_view()),
    re_path(r'^students/<id:int>', StudentApi.as_view()),
    re_path(r'^teachers/', TeacherApi.as_view()),
    re_path(r'^teachers/<id:int>', TeacherApi.as_view()),
    re_path(r'^positions/', PositionApi.as_view()),
    re_path(r'^specs/', SpecializationApi.as_view()),
]