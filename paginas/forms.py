from django import forms
from paginas.models import tb_balanco

class empforms(forms.ModelForm):
    class Meta:
        model=tb_balanco
        fields="__all__"
