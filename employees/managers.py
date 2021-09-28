from django.db import models

class EmpleadosManager(models.Manager):

    """ Managers para el modelo empleados """

    def buscar_empleado(self, kwords):

     
        if kwords == '':
            resultado = []
        else:
            resultado = self.filter(cedula=kwords)

        return resultado


    def buscar_nombre(self, kword):


        if kword== '':
            resultado = []
        else:
            resultado = self.filter(name__icontains=kword)

        return resultado
