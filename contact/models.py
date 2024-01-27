from django.db import models
from django.core.validators import EmailValidator, integer_validator


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=12)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


