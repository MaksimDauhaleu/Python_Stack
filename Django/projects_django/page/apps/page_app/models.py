from django.db import models


class Sneaker(models.Model):
    price = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    sneaker_image = models.ImageField(upload_to='gallery')

    def __str__(self):
        return self.name
