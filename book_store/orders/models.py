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


