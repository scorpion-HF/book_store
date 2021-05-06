from django.urls import path
from .views import AddToCartView, UserCartView, RemoveFromCartView, CreateOrderView

app_name = 'orders'
urlpatterns = [
    path('add_<int:pk>_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_<int:pk>_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/', UserCartView.as_view(), name='user_cart'),
    path('new_order/', CreateOrderView.as_view(), name='new_order'),
]
