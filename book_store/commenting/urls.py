from django.urls import path
from .views import CommentsListView

app_name = 'commenting'
urlpatterns = [
    path('book_<int:pk>/', CommentsListView.as_view(), name='comments_list'),
]