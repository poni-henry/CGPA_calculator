from django.db import models

# Create your models here.

from django.db import models

# Model to store students' details
class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    matriculation_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Model to store course details
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    credit_hours = models.IntegerField()

    def __str__(self):
        return self.name

# Model to store students' grades
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)  # 'A', 'B+', etc.

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade}"
