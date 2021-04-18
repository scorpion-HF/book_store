from django.urls import path, include
from .views import CommentsView

app_name = 'commenting'
urlpatterns = [
    path('book_<int:pk>/', CommentsView.as_view(), name='comments'),


]
