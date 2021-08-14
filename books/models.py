from django.db import models


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.title