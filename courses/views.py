from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Course,Enrollment,Lesson,LessonCompletion

def home(request):
    courses=Course.objects.filter(is_published=True)[:3]
    return render(request,'home.html',{'courses':courses})
def course_list(request):
    qs=Course.objects.filter(is_published=True)
    q=request.GET.get('q',''); level=request.GET.get('level','')
    if q: qs=qs.filter(Q(title__icontains=q)|Q(description__icontains=q)|Q(skills__icontains=q))
    if level: qs=qs.filter(level=level)
    return render(request,'courses/list.html',{'courses':qs,'q':q,'level':level})
def course_detail(request,slug):
    course=get_object_or_404(Course,slug=slug,is_published=True)
    enrolled=request.user.is_authenticated and Enrollment.objects.filter(student=request.user,course=course).exists()
    return render(request,'courses/detail.html',{'course':course,'enrolled':enrolled})
@login_required
def enroll(request,slug):
    course=get_object_or_404(Course,slug=slug,is_published=True)
    if request.method=='POST': Enrollment.objects.get_or_create(student=request.user,course=course); messages.success(request,'You are enrolled. Start learning!')
    return redirect('course_detail',slug=slug)
@login_required
def learning(request,slug):
    course=get_object_or_404(Course,slug=slug); enrollment=get_object_or_404(Enrollment,student=request.user,course=course)
    lessons=course.lessons.all(); completed=set(enrollment.completed_lessons.values_list('lesson_id',flat=True))
    percent=round(len(completed)/lessons.count()*100) if lessons.exists() else 0
    return render(request,'courses/learning.html',{'course':course,'enrollment':enrollment,'lessons':lessons,'completed':completed,'percent':percent})
@login_required
def complete_lesson(request,slug,lesson_id):
    if request.method=='POST':
        enrollment=get_object_or_404(Enrollment,student=request.user,course__slug=slug); lesson=get_object_or_404(Lesson,id=lesson_id,course=enrollment.course)
        LessonCompletion.objects.get_or_create(enrollment=enrollment,lesson=lesson)
        if enrollment.course.lessons.count()==enrollment.completed_lessons.count(): enrollment.completed=True; enrollment.save(update_fields=['completed'])
        messages.success(request,'Lesson progress saved.')
    return redirect('learning',slug=slug)
