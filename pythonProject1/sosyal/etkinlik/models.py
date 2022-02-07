from django.db import models

class Activate(models.Model):
    adi = models.CharField(max_length=200)
    turu = models.CharField(max_length=200)
    kapasite = models.IntegerField()
    tarih = models.DateField()


