from django import forms
from paginas.models import tb_balanco

class empforms(forms.ModelForm):
    class Meta:
        model=tb_balanco
        fields="__all__"

class InputForm(forms.ModelForm):
    lista = forms.CharField(max_length = 200)
    