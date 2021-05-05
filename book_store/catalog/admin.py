from django.contrib import admin
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Book, Author, Category


@admin.register(Book)
class FirstModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    # show jalali date in list display
    list_display = ['__str__', 'price', 'allow_comments', 'date_of_publish_jalali']
    filter_horizontal = ('authors', 'categories',)

    def date_of_publish_jalali(self, obj):
        return date2jalali(obj.date_of_publish).strftime('%y/%m/%d')

    date_of_publish_jalali.short_description = 'تاریخ ایجاد'
    date_of_publish_jalali.admin_order_field = 'created'


admin.site.register(Author)
admin.site.register(Category)
