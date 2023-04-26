from typing import Iterable, List
from django.http import JsonResponse, HttpRequest, QueryDict
from django.urls import re_path
from django.db import models
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.views import APIView
from schedule_app.services.uni_study_service import StudyLevelService, CourseService, StudyFormService, \
                                                    SubjectService, StatusTypeService, StudyGroupService, \
                                                    ExamService, LessonService, LessonTimesService, \
                                                    LessonStatusesService, StudyDayService

from schedule_app.serializers.uni_study_serializer import StudyLevelSerializer, CourseSerializer, StudyFormSerializer, \
                                                          SubjectSerializer, StatusTypeSerializer, StudyGroupSerializer, \
                                                          ExamSerializer, LessonSerializer, LessonTimesSerializer, \
                                                          LessonStatusesSerializer, StudyDaySerializer

class StudyLevelApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StudyLevelService()
        serializer = StudyLevelSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class CourseApi(APIView):
    def get(self, request) -> JsonResponse:
        service = CourseService()
        serializer = CourseSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyFormApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StudyFormService()
        serializer = StudyFormSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class SubjectApi(APIView):
    def get(self, request) -> JsonResponse:
        service = SubjectService()
        serializer = SubjectSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StatusTypeApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StatusTypeService()
        serializer = StatusTypeSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class LessonTimesApi(APIView):
    def get(self, request) -> JsonResponse:
        service = LessonTimesService()
        serializer = LessonTimesSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class StudyGroupApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StudyGroupService()
        service_data = None
        st_group_id: int | None = request.GET.get('id', None)
        many: bool = False

        if st_group_id:
            service_data = service.get_one(st_group_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = StudyGroupSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = StudyGroupSerializer(data=request.data, many=isinstance(request.data, List))
        service = StudyGroupService()

        if serializer.is_valid():
            service.create(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = StudyGroupService()
        st_group = service.get_one(request.query_params.get('id'))
        serializer = StudyGroupSerializer(st_group, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class ExamApi(APIView):
    def get(self, request) -> JsonResponse:
        service = ExamService()
        service_data = None
        exam_id: int | None = request.GET.get('id', None)
        many: bool = False

        if exam_id:
            service_data = service.get_one(exam_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = ExamSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = ExamSerializer(data=request.data, many=isinstance(request.data, List))
        service = ExamService()

        if serializer.is_valid():
            service.create(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = ExamService()
        exam = service.get_one(request.query_params.get('id'))
        serializer = ExamSerializer(exam, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class LessonApi(APIView):
    def get(self, request) -> JsonResponse:
        service = LessonService()
        service_data = None
        lesson_id: int | None = request.GET.get('id', None)
        many: bool = False

        if lesson_id:
            service_data = service.get_one(lesson_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = LessonSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = LessonSerializer(data=request.data, many=isinstance(request.data, List))
        service = LessonService()

        if serializer.is_valid():
            service.create(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = LessonService()
        lesson = service.get_one(request.query_params.get('id'))
        serializer = LessonSerializer(lesson, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class LessonStatusesApi(APIView):
    def get(self, request) -> JsonResponse:
        service = LessonStatusesService()
        service_data = None
        lesson_st_id: int | None = request.GET.get('id', None)
        many: bool = False

        if lesson_st_id:
            service_data = service.get_one(lesson_st_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = LessonStatusesSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = LessonStatusesSerializer(data=request.data, many=isinstance(request.data, List))
        service = LessonStatusesService()

        if serializer.is_valid():
            service.create(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = LessonStatusesService()
        lesson_st = service.get_one(request.query_params.get('id'))
        serializer = LessonStatusesSerializer(lesson_st, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class StudyDayApi(APIView):
    def get(self, request) -> JsonResponse:
        service = StudyDayService()
        service_data = None
        st_day_id: int | None = request.GET.get('id', None)
        many: bool = False

        if st_day_id:
            service_data = service.get_one(st_day_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = StudyDaySerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        serializer = StudyDaySerializer(data=request.data, many=isinstance(request.data, List))
        service = StudyDayService()

        if serializer.is_valid():
            service.create(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_201_CREATED})

        return JsonResponse({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = StudyDayService()
        st_day = service.get_one(request.query_params.get('id'))
        serializer = StudyDaySerializer(st_day, data=request.data, partial=True)

        if serializer.is_valid():
            service.update(serializer.validated_data)
            return JsonResponse({'success': 'updated'})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

urls = [
    re_path(r'^st_levels/', StudyLevelApi.as_view()),
    re_path(r'^courses/', CourseApi.as_view()),
    re_path(r'^st_forms/', StudyFormApi.as_view()),
    re_path(r'^subjects/', SubjectApi.as_view()),
    re_path(r'^status_types/', StatusTypeApi.as_view()),
    re_path(r'^less_times/', LessonTimesApi.as_view()),
    re_path(r'^st_groups/', StudyGroupApi.as_view()),
    re_path(r'^st_groups/<id:int>', StudyGroupApi.as_view()),
    re_path(r'^exams/', ExamApi.as_view()),
    re_path(r'^exams/<id:int>', ExamApi.as_view()),
    re_path(r'^lessons/', LessonApi.as_view()),
    re_path(r'^lessons/<id:int>', LessonApi.as_view()),
    re_path(r'^less_stats/', LessonStatusesApi.as_view()),
    re_path(r'^less_stats/<id:int>', LessonStatusesApi.as_view()),
    re_path(r'^st_days/', StudyDayApi.as_view()),
    re_path(r'^st_days/<id:int>', StudyDayApi.as_view()),
]