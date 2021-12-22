from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Category(models.Model):
    category = models.CharField(max_length=20, null=False, blank=False, primary_key=True,
                                verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'

    def __str__(self):
        return self.category


class Book(models.Model):
    image = ResizedImageField(size=[225, 225], crop=['bottom', 'right'], quality=100, upload_to='books_images/',
                              null=True, blank=True, verbose_name='تصویر')
    summery_file = models.FileField(upload_to='books_files/', null=True, blank=True, verbose_name='فایل')
    categories = models.ManyToManyField('Category', blank=False, verbose_name='دسته بندی ها')
    title = models.CharField(max_length=100, blank=False, null=False, verbose_name='عنوان')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    price = models.IntegerField(blank=False, verbose_name='قیمت')
    date_of_publish = models.DateField(verbose_name='سال چاپ')
    
    authors = models.ManyToManyField('Author', blank=False, verbose_name='نویسندگان')
    allow_comments = models.BooleanField(default=True, verbose_name='مجوز دریافت نظرات')

    class Meta:
        verbose_name = 'کتاب'
        verbose_name_plural = 'کتاب ها'

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام')
    last_name = models.CharField(max_length=50, blank=False, null=False, verbose_name='نام خانوادگی')

    class Meta:
        verbose_name = 'نویسنده'
        verbose_name_plural = 'نویسندگان'

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
