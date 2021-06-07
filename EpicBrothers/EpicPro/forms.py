from django import forms
from .models import contacto, Juegos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError



class contactoForm(forms.ModelForm):
    nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    
    class Meta:
        model = contacto
        #fields =["nombre", "correo", "tipo_consulta", "mensaje","avisos"]
        fields = '__all__'

class JuegosForm(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=50)
    imagen = forms.ImageField()
    precio = forms.IntegerField(min_value=1, max_value=1000000)

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        existe = Juegos.objects.filter(nombre__iexact=nombre).exists()

        if existe:
            raise ValidationError("Este juego ya existe, porfavor verifique la base de datos")
        return nombre


    class Meta:
        model = Juegos
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields =['username', "first_name", "last_name", "email", "password1", "password2"]
    