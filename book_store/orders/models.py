from django.db import models


class Cart(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=False)

    def get_total(self):
        cart_items = self.cartitem_set.all()
        total = 0
        for cart_item in cart_items:
            total += cart_item.item.price * cart_item.quantity
        return total


class CartItem(models.Model):
    item = models.ForeignKey('catalog.Book', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, null=False, blank=False)

    def get_total(self):
        return self.item.price * self.quantity


class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    is_posted = models.BooleanField(default=False, blank=False)
    address = models.TextField(blank=False, null=False)
    postal_code = models.CharField(max_length=10, blank=False, null=False, default=0)
    is_paid = models.BooleanField(default=False, blank=False)

    def get_total(self):
        order_items = self.orderitem_set.all()
        total = 0
        for order_item in order_items:
            total += order_item.item_price * order_item.item_quantity
        return total


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False)
    item_title = models.CharField(max_length=100, null=False, blank=False)
    item_price = models.IntegerField(blank=False, null=False)
    item_quantity = models.IntegerField(blank=False, null=False)

    def get_total(self):
        return self.item_price * self.item_quantity
