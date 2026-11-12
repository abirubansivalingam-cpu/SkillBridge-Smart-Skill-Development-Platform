# SkillBridge Testing Guide

## Automated checks
```cmd
python manage.py makemigrations accounts courses assessments progress
python manage.py migrate
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

## Load sample content
```cmd
python manage.py seed_demo
```

## Manual test checklist
- [ ] Register a learner account
- [ ] Log in and update career goal in Profile
- [ ] Browse/search courses and filter by level
- [ ] Open a course and enroll
- [ ] Open learning page and mark a lesson complete
- [ ] Confirm dashboard progress changes
- [ ] Open Assessments and submit a quiz
- [ ] Confirm score and pass/fail result
- [ ] Log out and log back in
- [ ] Log in to Django admin and manage course content

The sample content command creates three demo courses, lessons and basic quiz questions. The project is supplied as source; execute the checks in your own Python environment before submission.
