from django.shortcuts import render, get_object_or_404
from .models import Student

def student_results(request, student_id):
    student = get_object_or_404(Student, student_id=student_id)
    results = student.result_set.all()
    cgpa = student.calculate_cgpa()
    return render(request, 'results/student_results.html', {'student': student, 'results': results, 'cgpa': cgpa})
