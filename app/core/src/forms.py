from django import forms
from .pqrsf import Pqrsf
class Contacto(forms.Form):
    tipomensaje = forms.ChoiceField(label=" Tipo de peticion",required=True,choices=Pqrsf,widget=forms.Select(attrs={'class':'form-control'}))
    usuario = forms.CharField(label="Tu nombre",required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tu nombre'}))
    correo = forms.EmailField(label="Correo electronico",required=True, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Tu correo'}))
    mensaje = forms.CharField(label="Mensaje",required=True, widget=forms.Textarea(attrs={'class':'form-control','rows':'1','placeholder':'Tu mensaje'}))


