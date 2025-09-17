from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello.')

def home(request):
    return render(request, 'home.html', {'title': 'Home'})

def about(request):
    context = {
        'name': 'Cherry B. Custodio',
        'student_id': '2023-10715',
        'title': 'About'
    }
    return render(request, 'about.html', context)