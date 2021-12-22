from django.views.generic import ListView, DetailView

from .models import Book


class BooksListView(ListView):
    model = Book
    paginate_by = 12
    template_name = 'catalog/books_list.html'
    context_object_name = 'books'
    ordering = ['-date_of_publish']

    def get_queryset(self):
        term = self.request.GET.get('term')
        if term:
            self.queryset = Book.objects.filter(title__contains=term)
        return super().get_queryset()


class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    context_object_name = 'book'
