from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Enrollment
from .models import Quiz,QuizAttempt
@login_required
def quiz_list(request):
    enrolled=Enrollment.objects.filter(student=request.user).values_list('course_id',flat=True)
    quizzes=Quiz.objects.filter(course_id__in=enrolled).select_related('course')
    return render(request,'assessments/list.html',{'quizzes':quizzes})
@login_required
def take_quiz(request,quiz_id):
    quiz=get_object_or_404(Quiz.objects.prefetch_related('questions'),id=quiz_id)
    if not Enrollment.objects.filter(student=request.user,course=quiz.course).exists(): messages.error(request,'Enroll in this course before taking its quiz.'); return redirect('quiz_list')
    questions=list(quiz.questions.all())
    if request.method=='POST':
        score=sum(1 for q in questions if request.POST.get(f'q{q.id}')==q.correct_option)
        total=len(questions); passed=bool(total and score*100>=quiz.pass_mark*total)
        attempt=QuizAttempt.objects.create(student=request.user,quiz=quiz,score=score,total=total,passed=passed)
        return redirect('quiz_result',attempt_id=attempt.id)
    return render(request,'assessments/take.html',{'quiz':quiz,'questions':questions})
@login_required
def quiz_result(request,attempt_id):
    attempt=get_object_or_404(QuizAttempt,pk=attempt_id,student=request.user)
    return render(request,'assessments/result.html',{'attempt':attempt})
