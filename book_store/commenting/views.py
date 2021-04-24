from django.views.generic import DetailView
from catalog.models import Book


class CommentsListView(DetailView):
    model = Book
    template_name = 'commenting/comments_list.html'
    context_object_name = 'book'
