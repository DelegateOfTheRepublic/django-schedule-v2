from typing import List
from django.http import JsonResponse, HttpRequest, QueryDict
from django.urls import re_path
from rest_framework import status
from rest_framework.parsers import *
from rest_framework.views import APIView
from schedule_app.services.uni_general_service import FolderService, LinkService, LinkPlatformService, RoleService, Folder, TemplateService
from schedule_app.serializers.uni_general_serializer import LinkSerializer, LinkPlatformSerializer, RoleSerializer, FolderSerializer, TemplateSerializer

class RoleApi(APIView):
    def get(self, request) -> JsonResponse:
        service = RoleService()
        serializer = RoleSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

class FolderApi(APIView):
    def get(self, request) -> JsonResponse:
        service = FolderService()
        serializer = FolderSerializer(service.get_all(), many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = FolderService()
        serializer = FolderSerializer(data=request.data, many=isinstance(request.data, List), partial=True)

        if serializer.is_valid(raise_exception=True):
            service.create_folder(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = FolderService()
        serializer = FolderSerializer(data=request.data, partial=True)
        folder = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_folder(folder, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class LinkPlatformApi(APIView):
    def get(self, request) -> JsonResponse:
        service = LinkPlatformService()
        service_data = None
        link_plt_id: int | None = request.GET.get('id', None)
        many: bool = False

        if link_plt_id:
            service_data = service.get_one(link_plt_id)
            if service_data is None:
                return JsonResponse({'status': {
                    'code': status.HTTP_204_NO_CONTENT,
                    'message': 'no content'
                }})
        else:
            service_data = service.get_all()
            many = True

        serializer = LinkPlatformSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = LinkPlatformService()
        serializer = LinkPlatformSerializer(data=request.data, many=isinstance(request.data, List), partial=True)

        if serializer.is_valid(raise_exception=True):
            service.create_link_plt(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = LinkPlatformService()
        serializer = LinkPlatformSerializer(data=request.data, partial=True)
        link_plt = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_link_plt(link_plt, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class LinkApi(APIView):
    def get(self, request) -> JsonResponse:
        service = LinkService()
        service_data = None
        link_id: int | None = request.GET.get('id', None)
        many: bool = False

        if link_id:
            service_data = service.get_one(link_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = LinkSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = LinkService()
        serializer = LinkSerializer(data=request.data, many=isinstance(request.data, List), partial=True)

        if serializer.is_valid(raise_exception=True):
            service.create_link(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = LinkService()
        serializer = LinkSerializer(data=request.data, partial=True)
        link = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_link(link, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

class TemplateApi(APIView):
    def get(self, request) -> JsonResponse:
        service = TemplateService()
        service_data = None
        template_id: int | None = request.GET.get('id', None)
        many: bool = False

        if template_id:
            service_data = service.get_one(template_id)
        else:
            service_data = service.get_all()
            many = True

        serializer = TemplateSerializer(service_data, many=many)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request) -> JsonResponse:
        service = TemplateService()
        serializer = TemplateSerializer(data=request.data, many=isinstance(request.data, List), partial=True)

        if serializer.is_valid(raise_exception=True):
            service.create_template(serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

    def patch(self, request) -> JsonResponse:
        service = TemplateService()
        serializer = TemplateSerializer(data=request.data, partial=True)
        template = service.get_one(request.query_params.get('id'))

        if serializer.is_valid():
            service.update_template(template, serializer.validated_data)
            return JsonResponse({'status': status.HTTP_200_OK})

        return JsonResponse({'status': status.HTTP_400_BAD_REQUEST})

urls = [
    re_path(r'^roles/', RoleApi.as_view()),
    re_path(r'^link_plts/', LinkPlatformApi.as_view()),
    re_path(r'^link_plts/<id:int>', LinkPlatformApi.as_view()),
    re_path(r'^links/', LinkApi.as_view()),
    re_path(r'^links/<id:int>', LinkApi.as_view()),
    re_path(r'^folders/', FolderApi.as_view()),
    re_path(r'^folders/<id:int>', FolderApi.as_view()),
    re_path(r'^templates/', TemplateApi.as_view()),
    re_path(r'^templates/<id:int>', TemplateApi.as_view()),
]