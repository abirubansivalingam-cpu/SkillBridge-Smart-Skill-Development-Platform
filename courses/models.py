from django.db import models
from django.contrib.auth.models import User
class Course(models.Model):
    LEVELS=[('Beginner','Beginner'),('Intermediate','Intermediate'),('Advanced','Advanced')]
    title=models.CharField(max_length=180); slug=models.SlugField(unique=True); category=models.CharField(max_length=80,default='Technology')
    description=models.TextField(); skills=models.CharField(max_length=300,help_text='Comma-separated skills')
    level=models.CharField(max_length=20,choices=LEVELS,default='Beginner'); duration_hours=models.PositiveIntegerField(default=10)
    image_url=models.URLField(blank=True); is_published=models.BooleanField(default=True); created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
class Lesson(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons'); title=models.CharField(max_length=180)
    content=models.TextField(); video_url=models.URLField(blank=True); order=models.PositiveIntegerField(default=1)
    class Meta: ordering=['order']
    def __str__(self): return self.title
class Enrollment(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name='enrollments'); course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='enrollments')
    enrolled_at=models.DateTimeField(auto_now_add=True); completed=models.BooleanField(default=False)
    class Meta: unique_together=('student','course')
    def __str__(self): return f'{self.student} - {self.course}'
class LessonCompletion(models.Model):
    enrollment=models.ForeignKey(Enrollment,on_delete=models.CASCADE,related_name='completed_lessons'); lesson=models.ForeignKey(Lesson,on_delete=models.CASCADE)
    completed_at=models.DateTimeField(auto_now_add=True)
    class Meta: unique_together=('enrollment','lesson')
