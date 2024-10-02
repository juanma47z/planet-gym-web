from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['num_socio', 'nombre', 'apellido', 'dni', 'fecha_nacimiento', 'direccion', 'telefono', 'ocupacion', 'fecha_inicio', 'grupo_sanguineo', 'observaciones']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        # Si hay un valor inicial, asegúrate de formatear la fecha correctamente
        if self.instance and self.instance.pk:
            self.fields['fecha_nacimiento'].initial = self.instance.fecha_nacimiento.strftime('%Y-%m-%d')
            self.fields['fecha_inicio'].initial = self.instance.fecha_inicio.strftime('%Y-%m-%d')
