from django.apps import AppConfig


class OrdersConfig(AppConfig):
    name = 'orders'
    verbose_name = 'سفارش گیری'

    def ready(self):
        import orders.signals
