from django.contrib import admin
from .models import Course,Lesson,Enrollment,LessonCompletion
class LessonInline(admin.TabularInline): model=Lesson; extra=1
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin): list_display=('title','category','level','is_published'); prepopulated_fields={'slug':('title',)}; inlines=[LessonInline]
admin.site.register([Enrollment,LessonCompletion])
