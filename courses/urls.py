from django.urls import path
from . import views
urlpatterns=[path('',views.course_list,name='course_list'),path('<slug:slug>/',views.course_detail,name='course_detail'),path('<slug:slug>/enroll/',views.enroll,name='enroll'),path('<slug:slug>/learn/',views.learning,name='learning'),path('<slug:slug>/lesson/<int:lesson_id>/complete/',views.complete_lesson,name='complete_lesson')]
