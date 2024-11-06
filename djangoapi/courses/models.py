from django.db import models


# Create your models here.
class Course(models.Model):
    name: str = models.CharField(max_length=200)
    language: str = models.CharField(max_length=100)
    price: int = models.IntegerField(default=10)
    
    def __str__(self):
        return self.name