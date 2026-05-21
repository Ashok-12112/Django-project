from django.shortcuts import render
from .models import Student
students = Student.objects.all()


def home(request):
    return render(request,'home.html',{"student":students})

