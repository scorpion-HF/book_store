from django.db import models
from PIL import Image


class Book(models.Model):
    image = models.ImageField(upload_to='books_images/', null=True, blank=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(blank=False)
    data_of_publish = models.DateTimeField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            img = Image.open(self.image.path)
            output_size = (600, 600)
            img.thumbnail(output_size)
            img.save(self.image.path)
