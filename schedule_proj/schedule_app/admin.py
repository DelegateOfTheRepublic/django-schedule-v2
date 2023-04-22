from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Course)

admin.site.register(Department)
admin.site.register(DepartmentBoard)

admin.site.register(GroupSocialLink)

admin.site.register(LessonTimes)
admin.site.register(LessonStatuses)
admin.site.register(Lesson)
admin.site.register(Link)

admin.site.register(Position)
admin.site.register(Person)

admin.site.register(Role)
admin.site.register(RoomType)
admin.site.register(Room)

admin.site.register(StudyLevel)
admin.site.register(StudyGroup)
admin.site.register(StudyForm)
admin.site.register(StudyDay)
admin.site.register(Subject)
admin.site.register(Specialization)
admin.site.register(Student)
admin.site.register(StatusType)

admin.site.register(Template)
admin.site.register(Teacher)