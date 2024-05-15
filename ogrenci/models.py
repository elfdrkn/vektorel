from django.db import models

class Ogrenci(models.Model):
  TC = models.CharField(max_length=11)
  AdiSoyadi = models.CharField(max_length=50)
  Aciklama = models.CharField(max_length=255)

def __str__(self):
  return f"{self.AdiSoyadi} {self.Aciklama}"
