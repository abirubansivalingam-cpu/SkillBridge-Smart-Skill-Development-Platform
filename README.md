# SkillBridge – Smart Skill Development Platform

A Django-based learning platform for students to discover courses, enroll, complete lessons, take quizzes, and track learning progress. UI theme: dark navy with purple/cyan accents.

## Features
- Student registration, login/logout and profile/career goal
- Course catalogue with search and level filter
- Course details, enrollment and lesson completion tracking
- Student dashboard with enrollment and progress statistics
- Course quizzes, automatic scoring and pass/fail results
- Starter recommendation page based on the learner's stated career goal
- Django admin for managing courses, lessons, quizzes and questions
- SQLite default for easy setup; optional PostgreSQL configuration
- Responsive dark navy/purple UI

## Requirements
Python 3.11+ recommended, pip. PostgreSQL 14+ only if using PostgreSQL mode.

## Windows CMD setup
```cmd
cd %USERPROFILE%\Downloads\SkillBridge_Complete_Project
py -3.14 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py makemigrations accounts courses assessments progress
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/ . Admin: http://127.0.0.1:8000/admin/ .

## PostgreSQL (optional)
Create a database named `skillbridge_db`, then set these environment variables in CMD before running the server:
```cmd
set DB_ENGINE=postgres
set DB_NAME=skillbridge_db
set DB_USER=postgres
set DB_PASSWORD=YOUR_POSTGRES_PASSWORD
set DB_HOST=localhost
set DB_PORT=5432
python manage.py migrate
```
For a new CMD window, set the variables again or use a local `.env` loader of your choice. SQLite is the default and needs no database configuration.

## Add sample content
1. Create a superuser and log in to `/admin/`.
2. Add Course records with a unique slug (e.g. `python-foundations`), description, category, skills and duration.
3. Add Lesson records under each course. Set order values 1, 2, 3...
4. Add Quiz records for the course and add Questions with four options and correct option A/B/C/D.
5. Register a normal student, enroll in a course, mark lessons complete, then take its quiz.

## Test / verify
```cmd
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```
Manual checklist: register; log in; edit profile; search courses; enroll; open learning page; complete a lesson; verify dashboard progress; take a quiz; verify score; log out; verify admin management.

## Project structure
- `accounts`: user registration and profile
- `courses`: course catalogue, enrollment, lessons and completion
- `assessments`: quiz, questions and attempts
- `progress`: dashboard and recommendations
- `templates`: responsive page templates
- `static`: CSS and JavaScript

## Important notes
This is an academic starter application, not a production-hosted LMS. Course video hosting, email verification, payment processing, AI/LLM recommendations, proctored exams and certificate PDF signing are not implemented. Recommendations are transparent keyword-based suggestions, not a trained AI model. Before deployment, set a strong secret key, `DJANGO_DEBUG=0`, production `DJANGO_ALLOWED_HOSTS`, HTTPS/security settings, backups and a production web server.


## UI refresh (November 2026)
The refreshed package includes a consistent premium dark-navy interface with violet/cyan accents across the shared navigation, landing page, course catalogue, learning pages, assessments, dashboard, recommendations and account pages. The navigation collapses into an accessible mobile menu on smaller screens. Existing Django routes, models and workflows are preserved.
