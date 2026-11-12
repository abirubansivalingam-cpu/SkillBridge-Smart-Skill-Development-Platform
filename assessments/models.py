from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
class Quiz(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE,related_name='quizzes'); title=models.CharField(max_length=160); description=models.TextField(blank=True); pass_mark=models.PositiveIntegerField(default=60)
    def __str__(self): return self.title
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name='questions'); text=models.TextField(); option_a=models.CharField(max_length=240); option_b=models.CharField(max_length=240); option_c=models.CharField(max_length=240); option_d=models.CharField(max_length=240); correct_option=models.CharField(max_length=1,choices=[(x,x) for x in 'ABCD']); explanation=models.TextField(blank=True)
    def __str__(self): return self.text[:70]
class QuizAttempt(models.Model):
    student=models.ForeignKey(User,on_delete=models.CASCADE,related_name='quiz_attempts'); quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE); score=models.PositiveIntegerField(default=0); total=models.PositiveIntegerField(default=0); passed=models.BooleanField(default=False); attempted_at=models.DateTimeField(auto_now_add=True)
    @property
    def percentage(self): return round(self.score/self.total*100) if self.total else 0
