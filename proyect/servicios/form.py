from django import forms
from .models import Usuario, Servicio, Pedido

class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = "__all__"

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"

class PedidoForm(forms.ModelForm):
    usuario = forms.ModelChoiceField(
        queryset=Usuario.objects.all(),
        empty_label="Seleccione un usuario",
    )
    servicio = forms.ModelChoiceField(
        queryset=Servicio.objects.filter(estado=True),
        empty_label="Seleccione un servicio",
    )

    class Meta:
        model = Pedido
        fields = "__all__"
        widgets = {"fecha_entregado": forms.DateTimeInput(attrs={"type": "datetime-local"})}