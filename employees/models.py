from django.db import models

# Create your models here.
from .managers import EmpleadosManager


from home.models import Base
from departments.models import Departamento

class Empleados(Base):


    name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    cedula = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    city = models.CharField(max_length=30)
    department = models.ForeignKey(Departamento, related_name='dp', null=True, blank=True, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    objects = EmpleadosManager()


    def __str__(self):
        return self.name + self.last_name
