from pyexpat import model
from django import forms 
from .models import city


class CityForm(forms.ModelForm):
    
    class Meta:
        model = city
        fields = ("name",)

        name = forms.CharField(widget=forms.TextInput(attrs={
            'class':'input',
            'placeholer': 'enter city'
        }))
