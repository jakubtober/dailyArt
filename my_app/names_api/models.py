from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=64, null=False)
    last_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.name + ' ' + self.last_name
