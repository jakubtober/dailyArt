from uuid import uuid4
from django.db import models

# Create your models here.

class Person(models.Model):
    unique_id = models.CharField(max_length=256, default=uuid4())
    name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name
