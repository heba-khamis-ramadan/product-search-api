from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    price = models.FloatField()
    nutrition_facts = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
