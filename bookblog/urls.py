from django.urls import path

from . import views

app_name = 'bookblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('school/', views.school, name='school'),
    path('university/', views.university, name='university'),
    path('after/', views.after, name='after'),
    path('book_details/<book_id>', views.BookDetailsView.as_view(), name='book_details'),
    path('random_book/', views.random_book, name='random_book'),
    path('search/', views.SearchView.as_view(), name='search'),
]
