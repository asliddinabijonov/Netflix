from django.contrib.auth.models import AbstractUser
from django.db import models


class Aktyor(models.Model):
    ism = models.CharField(max_length=255)
    davlat = models.CharField(max_length=255, blank=True, null=True)
    jins = models.CharField(max_length=255)
    t_yil = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.ism


class Kino(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=50)
    yil = models.CharField(max_length=5)

    def __str__(self):
        return self.nom


class KinoAktyor(models.Model):
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    aktyor = models.ForeignKey(Aktyor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.kino.nom}: {self.aktyor.ism}"


class Tarif(models.Model):
    nom = models.CharField(max_length=255)
    narx = models.FloatField()
    davomiylik = models.CharField(max_length=50)


class User(AbstractUser):
    pass


class Izoh(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    matn = models.TextField(blank=True, null=True)
    baho = models.PositiveSmallIntegerField(default=5)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.kino.nom}"
