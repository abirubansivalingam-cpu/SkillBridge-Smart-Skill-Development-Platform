from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from courses.models import Enrollment
from assessments.models import QuizAttempt
@login_required
def dashboard(request):
    enrollments=Enrollment.objects.filter(student=request.user).select_related('course').prefetch_related('completed_lessons')
    rows=[]
    for e in enrollments:
        total=e.course.lessons.count(); done=e.completed_lessons.count(); percent=round(done/total*100) if total else 0
        rows.append({'enrollment':e,'percent':percent,'done':done,'total':total})
    attempts=QuizAttempt.objects.filter(student=request.user).select_related('quiz','quiz__course')[:5]
    return render(request,'progress/dashboard.html',{'rows':rows,'attempts':attempts,'enrolled_count':len(rows),'completed_count':sum(1 for x in rows if x['enrollment'].completed),'average_progress':round(sum(x['percent'] for x in rows)/len(rows)) if rows else 0})
@login_required
def recommendations(request):
    # Transparent starter recommendations based on skills entered in the profile.
    from courses.models import Course
    goal=request.user.profile.career_goal
    courses=Course.objects.filter(is_published=True)
    if goal: courses=courses.filter(skills__icontains=goal.split()[0])
    if not courses.exists(): courses=Course.objects.filter(is_published=True).order_by('level','title')[:6]
    return render(request,'progress/recommendations.html',{'courses':courses,'goal':goal})
