from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulario_view, name='formulario'),
    path('sucess/', views.sucess_view, name='sucess'),
    path('listar/', views.listar_formulario_view, name='listar_formularios'),
]
