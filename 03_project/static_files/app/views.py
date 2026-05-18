from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about/about.html')

def static(request):
    return render(request,'static.html')