from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Course,Lesson,Enrollment,LessonCompletion
class CourseFlowTests(TestCase):
    def setUp(self):
        self.user=User.objects.create_user(username='student',password='StrongPass!482')
        self.course=Course.objects.create(title='Python Basics',slug='python-basics',description='Learn Python',skills='Python',level='Beginner')
        self.lesson=Lesson.objects.create(course=self.course,title='Variables',content='Learn variables',order=1)
    def test_student_can_enroll_and_complete_lesson(self):
        self.client.login(username='student',password='StrongPass!482')
        response=self.client.post(reverse('enroll',args=[self.course.slug]))
        self.assertRedirects(response,reverse('course_detail',args=[self.course.slug]))
        enrollment=Enrollment.objects.get(student=self.user,course=self.course)
        self.client.post(reverse('complete_lesson',args=[self.course.slug,self.lesson.id]))
        self.assertEqual(LessonCompletion.objects.filter(enrollment=enrollment).count(),1)
        enrollment.refresh_from_db(); self.assertTrue(enrollment.completed)
