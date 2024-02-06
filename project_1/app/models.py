from django.db import models

class dept(models.Model):
    Depart = models.CharField(max_length=40, primary_key=True)

class datas(models.Model):
    NAME = models.CharField(max_length=30)
    EMAIL = models.CharField(max_length=30)
    PHONE=models.CharField(max_length=30, default=None)
    department = models.ForeignKey(dept, on_delete=models.CASCADE, default=None)


# Create your models here.

