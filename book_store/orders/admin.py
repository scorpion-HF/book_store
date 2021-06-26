from django.contrib import admin
from .models import CartItem, Cart, Order, OrderItem
from jalali_date import date2jalali


class OrderItemInline(admin.TabularInline):
    model = OrderItem


class CartItemInline(admin.StackedInline):
    model = CartItem


@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    inlines = [
        CartItemInline,
    ]
    list_display = ['cart_user', ]

    def cart_user(self, obj):
        return obj.user.get_full_name()

    cart_user.short_description = 'کاربر مربوطه'
    cart_user.admin_order_field = 'user'


@admin.register(CartItem)
class CartItemAdminModel(admin.ModelAdmin):
    pass



@admin.register(Order)
class OrderAdminModel(admin.ModelAdmin):
    inlines = [
        OrderItemInline,
    ]
    list_display = ['order_user', 'order_date', 'order_post_code', 'order_is_paid']
    list_filter = ['post_code', ]

    def order_user(self, obj):
        return obj.user.get_full_name()

    def order_date(self, obj):
        return date2jalali(obj.date).strftime('%y/%m/%d')

    def order_post_code(self, obj):
        return obj.post_code

    def order_is_paid(self, obj):
        if obj.is_paid:
            return 'پرداخت شد'
        return 'عدم پرداخت'

    order_user.short_description = 'سفارش دهنده'
    order_user.admin_order_field = 'user'

    order_date.short_description = 'تاریخ سفارش'
    order_date.admin_order_field = 'date'

    order_post_code.short_description = 'کد رهگیری پستی'
    order_post_code.admin_order_field = 'post_code'
    order_post_code.empty_value_display = 'ارسال نشده است'

    order_is_paid.short_description = 'وضعیت پرداخت'
    order_is_paid.admin_order_field = 'is_paid'


@admin.register(OrderItem)
class OrderItemAdminModel(admin.ModelAdmin):
    pass

