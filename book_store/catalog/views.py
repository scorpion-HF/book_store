from django.views.generic import ListView, DetailView
from .models import Book


class BooksListView(ListView):
    model = Book
    paginate_by = 10
    template_name = 'catalog/books_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'


class CommentsView(DetailView):
    model = Book
    template_name = 'catalog/comments.html'
    context_object_name = 'book'
