from django.urls import path, re_path
from .views import AddToCartView, UserCartView, RemoveFromCartView, CreateOrderView, UserOrdersView, OrderDetailView

'''from .views import send_request, verify'''

app_name = 'orders'
urlpatterns = [
    path('add_<int:pk>_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('remove_<int:pk>_from_cart/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('cart/', UserCartView.as_view(), name='user_cart'),
    path('orders/', UserOrdersView.as_view(), name='orders_list'),
    path('new_order/', CreateOrderView.as_view(), name='new_order'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    # re_path(r'^request/<int:order_id>/$', send_request, name='payment_request'),
    # re_path(r'^verify/<int:order_id>/$', verify, name='verify_payment'),
]
