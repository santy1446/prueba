from django.db import models


# Create your models here.
class Datos(models.Model):
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.descripcion)
