from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre = models.CharField(max_length=50)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return (f"Nombre: {self.nombre} - Edad: {self.edad} - Fecha de Nacimiento: {self.fecha_nacimiento}")