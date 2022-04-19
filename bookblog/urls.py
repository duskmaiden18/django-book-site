from django.urls import path

from . import views

app_name = 'bookblog'
urlpatterns = [
    path('', views.index, name='index'),
    path('school/', views.school, name='school'),
    path('university/', views.university, name='university'),
    path('after/', views.after, name='after'),
    path('book_details/<book_id>', views.BookDetails.as_view(), name='book_details'),
]
