from django.views.generic import DetailView
from catalog.models import Book


class CommentsView(DetailView):
    model = Book
    template_name = 'commenting/comments.html'
    context_object_name = 'book'
