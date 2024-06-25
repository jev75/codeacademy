from django.urls import path, include
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('search/', views.search, name='search'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my_borrowed'),
    path('register/', views.register, name='register')

]