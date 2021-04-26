from django import forms
from .models import *


class ShopForm(forms.ModelForm):

    # cover = forms.FileField(widget=form)

    class Meta:
        model = Shop
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shop Title'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shop Author'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shop Price',
                'type': 'number'
            }),
            'published_year': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Shop Author'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Shop Author'
            }),
            'cover': forms.FileInput(attrs={
                'class': 'form-control',

            })
        }