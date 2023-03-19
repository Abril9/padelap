from django import forms

from .models import Torneo, Usuario


class UsuarioForms(forms.ModelForm):
#    content = forms.CharField(label= '', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    nombre = forms.CharField(label= 'nombre', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    apellido = forms.CharField(label= 'apellido', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    email = forms.EmailField(label= 'email', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    wsp = forms.CharField(label= 'whatsapp', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    username = forms.CharField(label= 'username', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    password = forms.CharField(label= 'password', widget=forms.TexArea(attrs={'rows': 2}),required=True)
    
    
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'wsp', 'username', 'password',]