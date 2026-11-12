from django.core.management.base import BaseCommand
from django.utils.text import slugify
from courses.models import Course,Lesson
from assessments.models import Quiz,Question
class Command(BaseCommand):
    help='Create example courses, lessons and quizzes for demonstration'
    def handle(self,*args,**kwargs):
        samples=[('Python Programming Foundations','Programming','Learn Python syntax, variables, conditions, loops, functions and practical problem solving.','Python,Programming,Logic','Beginner',12,[('Getting started with Python','Install Python and understand the interpreter.'),('Variables and data types','Work with strings, numbers, lists and dictionaries.'),('Conditions and loops','Control program flow with if statements and loops.'),('Functions','Write reusable functions and organize code.')]),('Web Development Essentials','Web Development','Understand how modern websites are structured and styled with HTML, CSS and JavaScript.','HTML,CSS,JavaScript,Web','Beginner',15,[('HTML structure','Build semantic page structure with common HTML elements.'),('CSS styling','Use selectors, layout, flexbox and responsive design.'),('JavaScript basics','Add interaction with variables, functions and events.')]),('Database Skills with PostgreSQL','Database','Learn relational database concepts, SQL queries, joins and data modelling.','SQL,PostgreSQL,Database','Intermediate',10,[('Relational concepts','Understand tables, keys and relationships.'),('SQL queries','Use SELECT, INSERT, UPDATE and DELETE.'),('Joins and grouping','Combine related records and summarize data.')])]
        for title,cat,desc,skills,level,hours,lessons in samples:
            c,_=Course.objects.get_or_create(slug=slugify(title),defaults={'title':title,'category':cat,'description':desc,'skills':skills,'level':level,'duration_hours':hours,'is_published':True})
            for i,(lt,body) in enumerate(lessons,1): Lesson.objects.get_or_create(course=c,order=i,defaults={'title':lt,'content':body})
            q,_=Quiz.objects.get_or_create(course=c,title=f'{title} Knowledge Check',defaults={'description':'A short practice assessment to review the key concepts.','pass_mark':60})
            if not q.questions.exists():
                Question.objects.create(quiz=q,text='Which statement best describes the main purpose of this learning path?',option_a='To build and practise the listed foundational skills',option_b='To replace all practical experience',option_c='To avoid learning concepts',option_d='To guarantee a job without practice',correct_option='A',explanation='A learning path supports structured practice and skill development.')
                Question.objects.create(quiz=q,text='What is a useful way to improve a new technical skill?',option_a='Never practise',option_b='Build small projects and review mistakes',option_c='Skip fundamentals',option_d='Memorize without understanding',correct_option='B',explanation='Consistent hands-on practice helps strengthen understanding.')
        self.stdout.write(self.style.SUCCESS('Demo courses, lessons and quizzes created.'))
