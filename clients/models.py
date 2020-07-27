from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    costumer = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    balance = models.FloatField()

    def __str__(self):
        return self.first_name + ' ' + self.last_name
