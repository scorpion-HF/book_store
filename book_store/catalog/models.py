from django.db import models
from PIL import Image
from django.urls import reverse


class Book(models.Model):
    image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(blank=False)
    date_of_publish = models.DateField()
    allow_comments = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def get_absolute_url(self):
        return reverse('catalog:book_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title



