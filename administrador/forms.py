from django import forms
from django.db import models
from django.forms import fields, widgets


from employees.models import Empleados
from departments.models import Departamento

class EmpleadosForm(forms.ModelForm):

    class Meta:
        model = Empleados
        fields = ['name', 'last_name', 'cedula', 'age', 'city', 'department']
        labels = {'name': 'Nombre', 'last_name': 'Apellidos', 'cedula': 'Cédula', 'age':'Edad',
                  'city': 'Ciudad', 'department': 'Área de trabajo'}
        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })


class DepartamentoForm(forms.ModelForm):

    class Meta:
        model = Departamento
        fields = ['name', 'description']
        labels = {'name': 'Nombre', 'description': 'Descripción del departamento'}
        widget = {'description': forms.Textarea}
        

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update({
                    'class': 'form-control'
                })

