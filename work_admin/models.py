from django.contrib import admin
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Colors(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color


class Cart(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='cart')
    name = models.CharField(max_length=50)
    price = models.FloatField(validators=[MinValueValidator(0)])
    color = models.ForeignKey(Colors, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return self.name
