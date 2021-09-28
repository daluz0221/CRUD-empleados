from django.db import models

# Create your models here.

from .managers import DepartamentoManager

from home.models import Base

class Departamento(Base):


    name = models.CharField(max_length=45)
    description = models.CharField(max_length=400)
    
    objects = DepartamentoManager()




    def __str__(self):
        return self.name
