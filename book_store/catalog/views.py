from django.views.generic import ListView, DetailView
from .models import Book


class BooksListView(ListView):
    model = Book
    paginate_by = 2
    template_name = 'catalog/books_list.html'
    context_object_name = 'books'
    ordering = ['-date_of_publish']


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'
