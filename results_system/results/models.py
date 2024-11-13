from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.user.username} ({self.student_id})"
    
    def calculate_cgpa(self):
        results = Result.objects.filter(student=self)
        total_points = 0
        total_credit_hours = 0

        for result in results:
            if result.grade:  # Ensure there's a grade
                total_points += result.grade.points * result.course.credit_hours
                total_credit_hours += result.course.credit_hours

        return total_points / total_credit_hours if total_credit_hours > 0 else 0

class Course(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credit_hours = models.IntegerField()

    def __str__(self):
        return f"{self.code} - {self.name}"

class Grade(models.Model):
    grade = models.CharField(max_length=2)
    points = models.FloatField()  # Example: A = 4.0

    def __str__(self):
        return f"{self.grade} ({self.points})"

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.student} - {self.course} - {self.grade.grade}"
