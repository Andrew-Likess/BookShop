from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Passport(models.Model):
    series = models.IntegerField(validators=[
        MinValueValidator(10000),
        MaxValueValidator(90000)
    ])

class Author(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    passport = models.OneToOneField(Passport,on_delete=models.CASCADE)

class Book(models.Model):
    name = models.CharField(max_length=23)
    image = models.CharField(max_length=150, default="", null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=6, decimal_places=0)
