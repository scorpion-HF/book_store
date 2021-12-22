from django.views.generic import UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from .forms import ProfileForm


class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'users/profile.html'
    model = User
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user



