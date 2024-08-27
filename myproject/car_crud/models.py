from django.db import models

# Create your models here.

class Car(models.Model):
    car_name = models.CharField(max_length=100)
    mfg_year = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    kms_driven = models.IntegerField()
    owners = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.car_name