from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.exceptions import ValidationError
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.utils import timezone
from . import models

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'classe-a classe-b',
                'placeholder': 'Aqui veio do init',
            }
        ),
        label='Primeiro Nome',
        help_text='Texto de ajuda para seu usuário',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone',
            'email', 'description', 'category'
        )
    def clean(self):
        cleaned_data = self.cleaned_data
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )
            self.add_error('first_name', msg)
            self.add_error('last_name', msg)
        return super().clean()
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )
        return first_name
"""def create(request):
    if request.method == 'POST':
        context = {
            'form': ContactForm(request.POST)
        }
        return render(
            request,
            'contact/create.html',
            context
        )
    context = {
        'form': ContactForm()
    }
    return render(
        request,
        'contact/create.html')"""

