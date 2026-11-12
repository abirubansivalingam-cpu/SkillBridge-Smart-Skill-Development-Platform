from django.contrib import admin
from .models import Quiz,Question,QuizAttempt
class QuestionInline(admin.TabularInline): model=Question; extra=2
@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin): list_display=('title','course','pass_mark'); inlines=[QuestionInline]
admin.site.register(QuizAttempt)
