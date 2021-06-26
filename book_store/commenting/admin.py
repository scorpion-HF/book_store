from django.contrib import admin
from .models import BookComment
from jalali_date import date2jalali


@admin.register(BookComment)
class BookCommentModelAdmin(admin.ModelAdmin):
    list_display = ['username', 'name_of_user', 'book', 'submit_date_jalali']

    def username(self, obj):
        return obj.user.__str__()

    def name_of_user(self, obj):
        return obj.user.first_name+obj.user.last_name

    def book(self, obj):
        print(dir(obj))
        return obj.content_object.title

    def submit_date_jalali(self, obj):
        return date2jalali(obj.submit_date).strftime('%y/%m/%d')

    username.short_description = 'کاربر'
    username.admin_order_field = 'user'

    name_of_user.short_description = 'نام کاربر'
    name_of_user.admin_order_field = 'user__first_name'

    book.short_description = 'نام کتاب'

    submit_date_jalali.short_description = 'تاریخ ارسال'
    submit_date_jalali.admin_order_field = 'submit_date'


