from django.db import models

# Create your models here.


class ModelA(models.Model):
    name = models.CharField(max_length=100)


class ModelB(models.Model):
    name = models.CharField(max_length=100)



class ModelC(models.Model):
    name = models.CharField(max_length=100)