from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Book
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    return render(request, 'bookblog/index.html')

def school(request):
    contact_list = Book.objects.filter(type='school')
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'bookblog/school.html', {'page_obj': page_obj})

def university(request):
    return render(request, 'bookblog/university.html')

def after(request):
    return render(request, 'bookblog/after.html')

class BookDetails(View):

    def get(self, request, book_id):

        book = Book.objects.get(id=book_id)
        return render(request, 'bookblog/book_details.html', context={'book': book})



