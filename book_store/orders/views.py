import logging
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseGone
from django.views.generic import RedirectView, ListView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin
from catalog.models import Book
from .models import Cart, CartItem, Order, OrderItem
from django.shortcuts import reverse
from .forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin

logger = logging.getLogger('django.request')


class UserCartView(LoginRequiredMixin, ListView):
    template_name = 'orders/user_cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        self.cart, cart_created = Cart.objects.get_or_create(user=self.request.user)
        return self.cart.cartitem_set.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['cart'] = self.cart
        return context


class AddToCartView(LoginRequiredMixin, RedirectView, SingleObjectMixin):
    model = Book

    def get(self, request, *args, **kwargs):
        url = request.META.get('HTTP_REFERER')
        if url:
            if self.permanent:
                return HttpResponsePermanentRedirect(url)
            else:
                return HttpResponseRedirect(url)
        else:
            logger.warning(
                'Gone: %s', request.path,
                extra={'status_code': 410, 'request': request}
            )
            return HttpResponseGone()

    def post(self, request, *args, **kwargs):
        book = self.get_object()
        cart, cart_created = Cart.objects.get_or_create(
            user=request.user,
        )
        cart_item, cart_item_created = CartItem.objects.get_or_create(
            cart_id=cart.id,
            item=book
        )
        if not cart_item_created:
            cart_item.quantity += 1
            cart_item.save()
        messages.success(request, '۱ عدد کتاب "{}" به سبد خرید اضافه شد'.format(book.title))
        return self.get(request, *args, **kwargs)


class RemoveFromCartView(LoginRequiredMixin, DeleteView):
    model = CartItem

    def get_success_url(self):
        return reverse('orders:user_cart')


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = 'orders/create_order.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('orders:user_cart')

    def get_initial(self):
        self.initial['address'] = self.request.user.address
        self.initial['postal_code'] = self.request.user.postal_code
        return self.initial.copy()

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        return super().form_valid(form)

