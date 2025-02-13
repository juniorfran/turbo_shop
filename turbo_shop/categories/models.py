from django.db import models
from products.models import Product
# Create your models here.

class Category(models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField()
    productos = models.ManyToManyField(Product, blank=True)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    