from django.shortcuts import render, redirect
from .forms import FormularioForm
from .models import Formulario

def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucess')
        
    else:
        form = FormularioForm()
    return render(request, 'formulario_app/formulario.html', {'form': form})

def sucess_view(request):
    return render(request, 'formulario_app/sucess.html')

def listar_formulario_view(request):
    formularios = Formulario.objects.all()
    return render(request, 'formulario_app/listar_formulario.html', {'formularios': formularios})
