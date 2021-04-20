from django.urls import path
from .views import sent

app_name = 'commenting'
urlpatterns = [
    path('sent/', sent, name='comments-xtd-sent'),
]