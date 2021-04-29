from django.db import models


class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=False)
    date = models.DateTimeField(auto_now=True, null=False, blank=False)
    address = models.TextField(blank=False, null=False)
    is_paid = models.BooleanField(default=False)
    is_accepted = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)

    def get_total(self):
        order_items = self.orderitem_set.all()
        total = 0
        for order_item in order_items:
            total += order_item.item.price * order_item.quantity
        return total


class OrderItem(models.Model):
    item = models.ForeignKey('catalog.Book', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    Order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=False)
