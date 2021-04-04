from django.views.generic import ListView, DetailView
from .models import Book


class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'catalog/books_list.html'


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
