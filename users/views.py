from django.views.generic import UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import ProfileForm
from catalog.models import Book


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    model = User
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user
 
        
class UserElectronicBooksView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'users/electronic_books.html'
    context_object_name = 'electronic_books'

    def get_queryset(self):
        return self.request.user.owned_ebooks.all()



