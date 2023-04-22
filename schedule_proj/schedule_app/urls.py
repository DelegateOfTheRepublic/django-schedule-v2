from django.urls import include, re_path
from rest_framework.authtoken.views import obtain_auth_token
# from .views import CourseApi, DepartmentApi, DepartmentBoardApi, \
#                    LessonApi, LinkApi, MyProfileApi, PersonApi, PositionApi, \
#                    RoleApi, RoomApi, RoomTypeApi, SpecializationApi, \
#                    StudyDayApi, StudyFormatApi, StudyGroupApi, StudyLevelApi, SubjectApi, TeacherApi, UploadScheduleTemplatesApi

# urlpatterns = [
#     re_path(r'^auth/', include('djoser.urls')),
#     re_path(r'^auth/', include('djoser.urls.authtoken')),

#     re_path(r'^courses/$', CourseApi.as_view()),

#     re_path(r'^departments/$', DepartmentApi.as_view()),
#     re_path(r'^department_boards/$', DepartmentBoardApi.as_view()),

#     re_path(r'^lessons/$', LessonApi.as_view()),
#     re_path(r'^links/$', LinkApi.as_view()),

#     re_path(r'^positions/$', PositionApi.as_view()),

#     re_path(r'^persons/$', PersonApi.as_view()),
#     re_path(r'^teachers/$', TeacherApi.as_view()),

#     re_path(r'^profile/$', MyProfileApi.as_view()),

#     re_path(r'^roles/$', RoleApi.as_view()),
#     re_path(r'^room_types/$', RoomTypeApi.as_view()),
#     re_path(r'^rooms/$', RoomApi.as_view()),

#     re_path(r'^st_levels/$', StudyLevelApi.as_view()),
#     re_path(r'^st_groups/$', StudyGroupApi.as_view()),
#     re_path(r'^st_formats/$', StudyFormatApi.as_view()),

#     re_path(r'^st_days/$', StudyDayApi.as_view()),

#     re_path(r'^subjects/$', SubjectApi.as_view()),
#     re_path(r'^specializations/$', SpecializationApi.as_view()),

#     re_path(r'^upload_schedule_templates/$', UploadScheduleTemplatesApi.as_view())