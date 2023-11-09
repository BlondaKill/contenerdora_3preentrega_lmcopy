from django.db import models

# models :

class  Model_girl(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    height = models.FloatField()
    age = models.IntegerField()
    birthdate = models.DateField(null=True, blank=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    address = models.CharField(max_length=255)


class Client(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
