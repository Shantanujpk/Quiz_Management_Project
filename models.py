from django.db import models
from student_management_app.models import Student

class Course(models.Model): # Created class for quiz course.
    course_name = models.CharField(max_length=50)  # Changed variable name to be more descriptive
    question_number = models.PositiveIntegerField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Question(models.Model): # Created class for question within a course.
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.PositiveIntegerField()
    question = models.CharField(max_length=500)  # Changed variable name to be more descriptive
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    cat = (
        ('Option1', 'Option1'),
        ('Option2', 'Option2'),
        ('Option3', 'Option3'),
        ('Option4', 'Option4'),
    )
    correct_answer = models.CharField(max_length=200, choices=cat)  

class Result(models.Model): # Created class for result of a student in an exam
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Course, on_delete=models.CASCADE)
    marks_obtained = models.PositiveIntegerField()  
    date_submitted = models.DateTimeField(auto_now=True)
