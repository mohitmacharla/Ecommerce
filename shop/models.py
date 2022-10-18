import email
from unittest.util import _MAX_LENGTH
from xml.dom.minidom import CharacterData
from django.db import models
from django.forms import CharField

# Create your models here.
class Product(models.Model):
    def __str__(self):
        return self.title
    title=models.CharField(max_length=200)
    price=models.FloatField()
    discount=models.FloatField()
    category=CharField(max_length=200)
    des=models.TextField()
    image=models.CharField(max_length=300)

class Order(models.Model):
    items=models.CharField(max_length=1000)
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    address=models.CharField(max_length=1000)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    total=models.CharField(max_length=200)
