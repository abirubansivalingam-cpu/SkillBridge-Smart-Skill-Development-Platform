from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from courses.models import Course,Enrollment
from .models import Quiz,Question,QuizAttempt
class QuizFlowTests(TestCase):
    def test_quiz_is_scored_and_result_is_private(self):
        user=User.objects.create_user(username='student',password='StrongPass!482')
        course=Course.objects.create(title='Web Basics',slug='web-basics',description='Learn web',skills='HTML')
        Enrollment.objects.create(student=user,course=course)
        quiz=Quiz.objects.create(course=course,title='Basics quiz',pass_mark=60)
        q=Question.objects.create(quiz=quiz,text='HTML stands for?',option_a='HyperText Markup Language',option_b='High Text Machine Language',option_c='Home Tool Markup Language',option_d='Hyperlinks Text Management Language',correct_option='A')
        self.client.login(username='student',password='StrongPass!482')
        response=self.client.post(reverse('take_quiz',args=[quiz.id]),{f'q{q.id}':'A'})
        attempt=QuizAttempt.objects.get(student=user,quiz=quiz)
        self.assertRedirects(response,reverse('quiz_result',args=[attempt.id]))
        self.assertEqual(attempt.percentage,100); self.assertTrue(attempt.passed)
