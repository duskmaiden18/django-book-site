from django.shortcuts import render
import random
from .models import Book
from django.views import View
from django.core.paginator import Paginator
from django.http import JsonResponse

def index(request):
    return render(request, 'bookblog/index.html')

def school(request):
    book_list = Book.objects.filter(type='school')
    obj_paginator = Paginator(book_list, 2)
    page_number = request.GET.get('page')
    page_obj = obj_paginator.get_page(page_number)

    context = {
        'obj_paginator': obj_paginator,
        'page_obj' : page_obj,
    }

    if request.method == 'POST':
        chosen_page = request.POST.get('chosen_page', None)
        results = list(obj_paginator.page(chosen_page).object_list.values('id',
                                                                      'name',
                                                                      'author',
                                                                      'pub_year',
                                                                      'image',
                                                                      'plot'))
        return JsonResponse({"results": results})

    return render(request, 'bookblog/school.html', context)

def university(request):
    book_list = Book.objects.filter(type='university')
    obj_paginator = Paginator(book_list, 2)
    page_number = request.GET.get('page')
    page_obj = obj_paginator.get_page(page_number)

    context = {
        'obj_paginator': obj_paginator,
        'page_obj' : page_obj,
    }

    if request.method == 'POST':
        chosen_page = request.POST.get('chosen_page', None)
        results = list(obj_paginator.page(chosen_page).object_list.values('id',
                                                                      'name',
                                                                      'author',
                                                                      'pub_year',
                                                                      'image',
                                                                      'plot'))
        return JsonResponse({"results": results})

    return render(request, 'bookblog/university.html', context)

def after(request):
    book_list = Book.objects.filter(type='after')
    obj_paginator = Paginator(book_list, 2)
    page_number = request.GET.get('page')
    page_obj = obj_paginator.get_page(page_number)

    context = {
        'obj_paginator': obj_paginator,
        'page_obj': page_obj,
    }

    if request.method == 'POST':
        chosen_page = request.POST.get('chosen_page', None)
        results = list(obj_paginator.page(chosen_page).object_list.values('id',
                                                                          'name',
                                                                          'author',
                                                                          'pub_year',
                                                                          'image',
                                                                          'plot'))
        return JsonResponse({"results": results})

    return render(request, 'bookblog/after.html', context)

class BookDetailsView(View):

    def get(self, request, book_id):

        book = Book.objects.get(id=book_id)
        return render(request, 'bookblog/book_details.html', context={'book': book})

def random_book(request):
    book_amount = Book.objects.all().count()
    random_book_id = random.randint(1, book_amount)
    book = Book.objects.get(id = random_book_id)

    return render(request, 'bookblog/book_details.html', context={'book': book})

class SearchView(View):

    def get(self, request):
        query = self.request.GET.get('book_name')
        book = Book.objects.get(name=query)
        return render(request, 'bookblog/book_details.html', context={'book': book})





