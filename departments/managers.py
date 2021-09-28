from django.db import models

class DepartamentoManager(models.Manager):

    """ Managers para el modelo empleados """

    def buscar_dpto(self, kwords):

     
        if kwords == '':
            resultado = []
        else:
            resultado = self.filter(
                name__icontains=kwords
            )
       

        return resultado