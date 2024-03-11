from django.db import models


class Product(models.Model):
    name = models.CharField(verbose_name="Name", max_length=40)
    price = models.IntegerField(verbose_name="Price")
    description = models.TextField(verbose_name="Description")
    image = models.ImageField(verbose_name="Image")
    type_id = models.OneToOneField("product.Type", on_delete=models.CASCADE)
    availability = models.CharField(verbose_name="Avalibility")


class Type(models.Model):
    type_name = models.CharField(verbose_name="Type Name", max_length=20)
