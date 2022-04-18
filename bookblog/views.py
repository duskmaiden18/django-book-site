from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    return render(request, 'bookblog/index.html')

def school(request):
    return render(request, 'bookblog/school.html')

def university(request):
    return render(request, 'bookblog/university.html')

def after(request):
    return render(request, 'bookblog/after.html')

def book_details(request):
    return render(request, 'bookblog/book_details.html')



