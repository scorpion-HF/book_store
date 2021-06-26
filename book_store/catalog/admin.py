from django.contrib import admin
from jalali_date import date2jalali
from jalali_date.admin import ModelAdminJalaliMixin
from .models import Book, Author, Category


@admin.register(Book)
class BookModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'date_of_publish_jalali']
    filter_horizontal = ('authors', 'categories',)

    def date_of_publish_jalali(self, obj):
        return date2jalali(obj.date_of_publish).strftime('%y/%m/%d')

    date_of_publish_jalali.short_description = 'تاریخ چاپ'
    date_of_publish_jalali.admin_order_field = 'date_of_publish'


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', ]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['category', ]
