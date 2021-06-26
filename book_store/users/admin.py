from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff_user')
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name', 'phone_number', 'address', 'postal_code',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active')}
        ),
    )
    ordering = ('email',)

    def is_staff_user(self, obj):
        if obj.is_staff:
            return 'کاربر ادمین'
        return 'کاربر عادی'

    is_staff_user.short_description = 'نوع کاربر'
    is_staff_user.admin_order_field = 'is_staff'


