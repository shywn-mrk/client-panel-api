from django.db import models
from django.contrib.auth.models import User

class Settings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    allow_registeration = models.BooleanField(default=False)
    disable_balance_on_add = models.BooleanField(default=False)
    disable_balance_on_edit = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
