from django.db import models
from django.urls import reverse
from django_resized import ResizedImageField


class Book(models.Model):
    image = ResizedImageField(size=[225, 225], crop=['bottom', 'right'], quality=100, upload_to='books_images/', null=True, blank=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(blank=False)
    date_of_publish = models.DateField()
    allow_comments = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title
