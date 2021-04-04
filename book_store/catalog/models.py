from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(null=True, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    price = models.IntegerField(blank=False)
    data_of_publish = models.DateTimeField()
