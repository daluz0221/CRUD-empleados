from django.db import models
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView,
   
    ListView,
    CreateView,
    DetailView,
    DeleteView,
    UpdateView
)

# Create your views here.

from .forms import EmpleadosForm, DepartamentoForm


from home.models import Home
from employees.models import Empleados
from departments.models import Departamento

class HomeView(TemplateView):

    template_name = 'home.html'
  
    
    def get_context_data(self,*args, **kwargs): 
        context = super(HomeView, self).get_context_data(*args,**kwargs)
        context['obj'] = Home.objects.first()
        
        return context

class AdminView(LoginRequiredMixin,TemplateView):
    template_name = 'admin.html'
    login_url = '/login'


class EmpleadoList(ListView):

    queryset = Empleados.objects.filter(active=True)
    template_name = 'empleado_list.html'
    context_object_name = 'obj'
    paginate_by = 4



class EmpleadoList2(LoginRequiredMixin,ListView):

    queryset = Empleados.objects.filter(active=True)
    template_name = 'admin-empleado_list.html'
    context_object_name = 'obj'
    paginate_by = 4
    login_url = '/login'

class EmpleadosNewView(LoginRequiredMixin, CreateView):

    model = Empleados
    template_name = 'admin-empleado_new.html'
    context_object_name = 'obj'
    form_class = EmpleadosForm
    success_url = reverse_lazy("administrador:admin-empleados_list")
    login_url = '/login'

class EmpleadosEditView(LoginRequiredMixin, UpdateView):

    model = Empleados
    template_name = 'admin-empleado_new.html'
    context_object_name = 'obj'
    form_class = EmpleadosForm
    success_url = reverse_lazy("administrador:admin-empleados_list")
    login_url = '/login'

class EmpleadoEditSearch(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    template_name= 'admin-empleado_form.html'
    login_url = '/login'

    def get_queryset(self):
        cedula = self.request.GET.get("kwords", '')
        print(cedula)
        nombre = self.request.GET.get("name", '')
        if cedula != '':
            return Empleados.objects.buscar_empleado(cedula)
        else:
            return Empleados.objects.buscar_nombre(nombre)






class DepartamentoList(ListView):

    model = Departamento
    template_name = 'departamento_list.html'
    context_object_name = 'obj'
    paginate_by = 2

class DepartamentoList2(DepartamentoList):

 
    template_name = 'admin-departamento_list.html'

    

    def get_context_data(self, **kwargs):

        return super().get_context_data(**kwargs)



class DepartamentoNewView(LoginRequiredMixin, CreateView):

    model = Departamento
    template_name = 'admin-dpto_new.html'
    context_object_name = 'obj'
    form_class = DepartamentoForm
    success_url = reverse_lazy("administrador:admin-departamento_list")
    login_url = '/login'



class DepartamentoEditView(LoginRequiredMixin, UpdateView):

    model = Departamento
    template_name = 'admin-dpto_new.html'
    context_object_name = 'obj'
    form_class = DepartamentoForm
    success_url = reverse_lazy("administrador:admin-departamento_list")
    login_url = '/login'



class DepartamentoEditSearch(LoginRequiredMixin, ListView):
    context_object_name = 'obj'
    template_name= 'admin-dpto_form.html'
    login_url = '/login'

    def get_queryset(self):
        nombre = self.request.GET.get("kwords", '')
        
        return Departamento.objects.buscar_dpto(nombre)


class DepartamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Departamento
    template_name = 'dpto_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy("administrador:admin-departamento_list")
     

class DepartamentoDetail(DetailView):

    model = Departamento
    template_name = 'departamento_detalle.html'
    context_object_name = 'obj'






def empleado_inactivo(request, id):

    empleado = Empleados.objects.filter(pk=id).first()
    
    contexto = {}

    if not empleado:
        return redirect("administrador:admin-empleados_list")


    if request.method == 'GET':
        contexto = {'obj': empleado}

    if request.method == 'POST':
        empleado.active = False
        empleado.department = None
        empleado.save()
        return redirect("administrador:admin-empleados_list")

    return render(request, 'empleado_del.html', contexto)

    