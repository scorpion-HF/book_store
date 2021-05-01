from django.urls import path
from .views import AddToCartView

app_name = 'orders'
urlpatterns = [
    path('add_<int:pk>_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
]
