from django.urls import path
from .views import BooksListView, BookDetailView, ElectronicBookView

app_name = 'catalog'
urlpatterns = [
    path('books_list/', BooksListView.as_view(), name='books_list'),
    path('book_<int:pk>_detail/', BookDetailView.as_view(), name='book_detail'),
    path('electronic_book_<int:pk>/', ElectronicBookView.as_view(), name='electronic_book'),
]
