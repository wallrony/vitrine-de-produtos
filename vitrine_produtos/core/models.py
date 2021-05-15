from django.db import models

from .utils import change_image_name


class ProductCategory(models.Model):
    name = models.CharField(max_length=50, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.TextField(blank=True, default=None, null=True)
    price = models.FloatField(blank=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ProductImage(models.Model):
    image = models.ImageField(upload_to=change_image_name, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

