from django import forms
from .models import Produto


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = [
            'nome_produto',
        ]
        widgets = {
            'nome_produto': forms.TextInput(
                attrs={
                    'class': 'form-control w-100',
                    'placeholder': 'Nome do Produto',
                }
            ),
        }
