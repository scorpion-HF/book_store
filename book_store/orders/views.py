import logging
from django.contrib import messages
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseGone
from django.views.generic import RedirectView, ListView, DeleteView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectMixin, DetailView
from catalog.models import Book
from .models import Cart, CartItem, Order, OrderItem
from django.shortcuts import reverse
from .forms import OrderForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from django.conf import settings

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
        return reverse('orders:payment_request', args=[self.object.id])

    def get_initial(self):
        self.initial['address'] = self.request.user.address
        self.initial['postal_code'] = self.request.user.postal_code
        return self.initial.copy()

    def form_valid(self, form):
        self.object = form.save()
        self.object.user = self.request.user
        self.object.save()
        cart, cart_created = Cart.objects.get_or_create(user=self.request.user)
        cart_items = cart.cartitem_set.all()
        for cart_item in cart_items:
            order_item = OrderItem.objects.create(order=self.object,
                                                  item_title=cart_item.item.title,
                                                  item_price=cart_item.item.price,
                                                  item_quantity=cart_item.quantity)
            order_item.save()
            cart_item.delete()
        return super().form_valid(form)


class UserOrdersView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'orders/user_orders.html'
    context_object_name = 'orders'


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = 'orders/order_detail.html'
    context_object_name = 'order'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['order_items'] = context['order'].orderitem_set.all()
        return context


def send_request(request, order_id):
    order = Order.objects.get(id=order_id)
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    result = client.service.PaymentRequest(settings.MERCHANT, order.get_total() / 10,
                                           'پرداخت مربوط به سفارش با کد{}'.format(order_id),
                                           request.user.email, request.user.phone_number,
                                           'http://localhost:8000/orders/verify/{}/'.format(order_id))
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request, order_id):
    order = Order.objects.get(id=order_id)
    client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(settings.MERCHANT, request.GET['Authority'], order.get_total() / 10)
        if result.Status == 100:
            order.is_paid = True
            order.save()
            messages.success(request, 'پرداخت با موفقیت انجام شد')
            return redirect('orders:order_detail', order_id)
        elif result.Status == 101:
            order.is_paid = True
            order.save()
            messages.success(request, 'تراکنش معتبر است:101 ')
            return redirect('orders:order_detail', order_id)
        else:
            messages.error(request, 'عملیات پرداخت با خطا مواجه شد')
            return redirect('orders:order_detail', order_id)
    else:
        messages.error(request, 'عملیات پرداخت با خطا مواجه شد')
        return redirect('orders:order_detail', order_id)
