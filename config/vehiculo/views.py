from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vehiculo

from django.shortcuts import render
from tokenize import PseudoExtras
# Create your views here.
from django.views.generic import TemplateView
from .forms import NameForm, InputForm, VehiculoForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth import login,authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
# importaremos decoradores
from django.contrib.auth.decorators import login_required, permission_required 
#decorador que exige al usuario ser staff para ingresar a la vista
from django.contrib.admin.views.decorators import staff_member_required

#gestionar permisos
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
# importamos el mixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
import datetime


# Create your views here.

def index(request):
    return render(request, 'index.html')
    # return HttpResponse("Hola Alejandra")

def menu_view(request):
    template_name = 'menu.html'
    return render(request, template_name)

def catalogo_view(request):
    vehiculos = Vehiculo.objects.all()
    return render(request, 'catalogo.html', context={'vehiculos':vehiculos})

def logout_view(request):
    logout(request)
    messages.info(request, "Seha cerrado la sesion satisfactoriamente.")
    return HttpResponseRedirect('/menu')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.info(request, f"iniciaste sesion como: {username}.")
                return HttpResponseRedirect('/')
            else:
                messages.error(request,"username o password Incorrectos")
                return HttpResponseRedirect('/login')
        else:
            messages.error(request,"username o password Incorrectos")
            return HttpResponseRedirect('/login')
    form = AuthenticationForm()
    context = {'login_form':form}
    return render(request, 'login.html', context)

def register_view(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            #obtenemos el contenttype del modelo
            content_type = ContentType.objects.get_for_model(Vehiculo)
            #obtenemos el permiso a asignar
            visualizador = Permission.objects.get(
                codename='visualizar_catalogo',
                content_type=content_type
            )
            user = form.save()
            #Agregar el permiso al usuario en el momento del registro
            user.user_permissions.add(visualizador)
            login(request, user)
            messages.success(request, "registrado satisfactoriamente")
        else:
            messages.error(request, "Registro invalido. Algunos datos ingresados no son correctos")
        return HttpResponseRedirect('/menu/') 
    
    form = UserRegisterForm()
    context = {"register_form": form}
    return render(request,"registro.html", context)