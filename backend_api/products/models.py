from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    shipping_details = models.CharField(max_length=100)
    images = models.JSONField()
    category = models.CharField(max_length=50)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name