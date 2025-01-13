from django.shortcuts import render, redirect
from .models import Student, Attendance
from datetime import date

# Admin Page: View all students
def admin_page(request):
    students = Student.objects.all()
    return render(request, 'admin_page.html', {'students': students})

# Attendance Page: Mark attendance
def attendance_page(request):
    message = None
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        try:
            student = Student.objects.get(id=student_id)
            # Check if attendance is already marked
            if Attendance.objects.filter(student=student, date=date.today()).exists():
                message = f"{student.name} has already marked attendance for today."
            else:
                Attendance.objects.create(student=student)
                message = f"Attendance marked for {student.name}."
        except Student.DoesNotExist:
            message = "Student ID not found."

    return render(request, 'attendance_page.html', {'message': message})
