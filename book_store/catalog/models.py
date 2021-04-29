from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Category(models.Model):
    category = models.CharField(max_length=1, null=False, blank=False, primary_key=True)


class Book(models.Model):
    image = ResizedImageField(size=[225, 225], crop=['bottom', 'right'], quality=100, upload_to='books_images/',
                              null=True, blank=True)
    category = models.ManyToManyField('category', blank=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(blank=False)
    date_of_publish = models.DateField()
    type = models.CharField(max_length=1, null=False, blank=False, default='p', choices=(
        ('p', 'نسخه چاپی'),
        ('a', 'نسخه صوتی'),
    ))
    authors = models.ManyToManyField('author', blank=False)
    allow_comments = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)

    def get_full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
