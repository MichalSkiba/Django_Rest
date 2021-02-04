from django.db import models


class Book(models.Model):
    autor = models.CharField(max_length=255)
    cena = models.IntegerField(null=True)
    jakosc = models.CharField(max_length=255)
    stron = models.IntegerField()
    tytul = models.CharField(max_length=255)
    url = models.CharField(max_length=255, null=True)
    url2 = models.CharField(max_length=255, null=True)
