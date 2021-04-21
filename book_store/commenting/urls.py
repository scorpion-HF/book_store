from django.urls import path
from .views import sent, CommentsListView

app_name = 'commenting'
urlpatterns = [
    path('sent/', sent, name='comments-xtd-sent'),
    path('book_<int:pk>_comments_list/', CommentsListView.as_view(), name='comments_list'),
]