from django.shortcuts import render, redirect
from .models import Usuario, Servicio, Pedido
from .form import UsuarioForm, ServicioForm, PedidoForm
def index(request):
    return render(request, "servicios/index.html")

def usuario_list(request):
    query = Usuario.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/usuario_list.html", context)

def servicio_list(request):
    query = Servicio.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/servicio_list.html", context)

def pedido_list(request):
    query = Pedido.objects.all()
    context = {"object_list": query}
    return render(request, "servicios/pedido_list.html", context)

def usuario_create(request):
    if request.method == "GET":
        form = UsuarioForm()
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("usuario_list")
    return render(request, "servicios/usuario_create.html", {"form": form})

def servicio_create(request):
    if request.method == "GET":
        form = ServicioForm()
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicio_list")
    return render(request, "servicios/servicio_create.html", {"form": form})

def pedido_create(request):
    if request.method == "GET":
        form = PedidoForm()
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pedido_list")
    return render(request, "servicios/pedido_create.html", {"form": form})
