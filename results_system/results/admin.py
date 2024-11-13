from django.contrib import admin
from .models import Student, Course, Grade, Result

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Grade)
admin.site.register(Result)
