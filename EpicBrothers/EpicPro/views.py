from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Juegos
from .forms import contactoForm, JuegosForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import JuegosSerializer


# Create your views here.

class JuegosViewset(viewsets.ModelViewSet):
    queryset = Juegos.objects.all()
    serializer_class = JuegosSerializer


    
def error_facebook(request):
    return render(request, 'registrarion/error_facebook.html')

def home(request):
    return render(request, "EpicPro/home.html") 

def servicios(request):
    return render(request,"EpicPro/servicios.html") 

def tienda(request):

    return render(request,"EpicPro/tienda.html") 

def blog(request):
    return render(request,"EpicPro/blog.html") 

def contacto(request):
    data = {
        'form': contactoForm()
    }
    
    if request.method == 'POST':
         formulario = contactoForm(data=request.POST)
         if formulario.is_valid():
             formulario.save()
             data["mensaje"] = "Enviado"
         else: 
             data["form"] = formulario

    return render(request,"EpicPro/contacto.html", data) 

def juegos(request):
    juegos = Juegos.objects.all()
    data= {
        'juegos': juegos
    }
    return render(request,"EpicPro/juegos.html", data) 


@permission_required('EpicPro.add_juegos')
def agregar(request):

    data ={
        'form': JuegosForm()
    }

    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Guardado Correctamente")
        else:
            data["form"] = formulario

    return render(request,"EpicPro/agregar.html", data)


@permission_required('EpicPro.view_juegos')
def listar(request):
    juegos=Juegos.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(juegos, 3)
        juegos = paginator.page(page)
    except:
        raise Http404


    data={
        'entity':juegos,
        'paginator': paginator
    }
    return render(request,"EpicPro/listar.html", data)


@permission_required('EpicPro.change_juegos')
def modificar(request, id):

    juegos =get_object_or_404(Juegos, id=id)
    data ={
        'form':JuegosForm(instance=juegos)
    }

    if request.method == 'POST':
        formulario = JuegosForm(data=request.POST, instance=juegos, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar")
        data["form"]= formulario
    return render(request,"EpicPro/modificar.html", data)


@permission_required('EpicPro.delete_juegos')
def eliminar(request, id):
    juegos = get_object_or_404(Juegos, id=id)
    juegos.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar")


def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="Home")
        data["form"] = formulario

    return render(request, 'registration/registro.html', data)

        

