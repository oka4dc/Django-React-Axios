from django.db import models

# Create your models here.
class React(models.Model):
    Employee = models.CharField(max_length=100)
    Department = models.CharField(max_length=150)



