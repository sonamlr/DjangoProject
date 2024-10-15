from django.shortcuts import render
from django.contrib import redirects
from .models import Student
from .forms import StudentRegistration
# Create your views here.
def student_list(request):
    stu = Student.objects.all()
    return render(request, 'list.html', {'stu':stu })

def add_student(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return redirects('/')
    else:
        fm = StudentRegistration()
    return render(request, 'add.html', {'form': fm})

def edit_student(request, pk):
    if request.method == 'POST':
        stu = Student.objects.get(pk=pk)
        fm = StudentRegistration(request.POST, instance=stu)
        if fm.is_valid():
            fm.save()
            return redirects('/')
    else:
        stu = Student.objects.get(pk=pk)
        fm = StudentRegistration(instance=stu)
    return render(request, 'edit.html', {'pk': pk, 'form': fm})

def delete_student(request):
    return redirects('/')