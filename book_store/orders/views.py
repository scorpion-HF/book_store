import logging
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseGone
from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin
from catalog.models import Book
from .models import Order, OrderItem

logger = logging.getLogger('django.request')


class AddToCartView(RedirectView, SingleObjectMixin):
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
        order, order_created = Order.objects.get_or_create(
            user=request.user,
            is_open=True
        )
        order_item, order_item_created = OrderItem.objects.get_or_create(
            order_id=order.id,
            item=book
        )
        if not order_item_created:
            order_item.quantity += 1
            order_item.save()
        return self.get(request, *args, **kwargs)
