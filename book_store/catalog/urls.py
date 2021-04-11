from django.urls import path
from .views import BooksListView, BookDetailView
app_name = 'catalog'
urlpatterns = [
    path('books_list/', BooksListView.as_view(), name='books_list'),
    path('book_<int:pk>_detail/', BookDetailView.as_view(), name='book_detail'),
]
