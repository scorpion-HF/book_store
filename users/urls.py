from django.urls import path
from .views import UserProfileView, UserElectronicBooksView
app_name = 'users'
urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('ebooks/', UserElectronicBooksView.as_view(), name='user_ebooks'),
]
