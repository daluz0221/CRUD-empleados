from django.urls import path
from django.views.generic.base import View
from django.contrib.auth import views as auth


from . import views


app_name = 'administrador'



urlpatterns=[
    path('', views.HomeView.as_view(), name='home'),

    path('admin/', views.AdminView.as_view(), name='admin'),
    path('admin/empleados/', views.EmpleadoList2.as_view(), name='admin-empleados_list'),
    path('admin/empleados/nuevo', views.EmpleadosNewView.as_view(), name='admin-empleados_new'),
    path('admin/empleados/edit', views.EmpleadoEditSearch.as_view(), name='admin-empleados_editSearch'),
    path('admin/empleados/edit/<int:pk>', views.EmpleadosEditView.as_view(), name='admin-empleados_edit'),
    path('admin/empleados/del/<int:id>', views.empleado_inactivo, name='admin-empleado_del'),

    path('admin/departamentos', views.DepartamentoList2.as_view(), name='admin-departamento_list'),
    path('admin/departamentos/nuevo', views.DepartamentoNewView.as_view(), name='admin-departamento_new'),
    path('admin/departamentos/edit', views.DepartamentoEditSearch.as_view(), name='admin-departamento_editsearch'),
    path('admin/departamentos/edit/<int:pk>', views.DepartamentoEditView.as_view(), name='admin-departamento_edit'),
    path('admin/departamento/delete/<int:pk>', views.DepartamentoDeleteView.as_view(), name='admin-dpto_del'),


    path('login/', auth.LoginView.as_view(template_name='login.html'), name="login"),
    path('logout/', auth.LogoutView.as_view(template_name='login.html'), name="logout"),
    path('empleados/', views.EmpleadoList.as_view(), name='empleados_list'),
    path('departamentos/', views.DepartamentoList.as_view(), name='departamentos_list'),
    path('departamentos/<pk>/', views.DepartamentoDetail.as_view(), name='departamento_detalle'),
    
]