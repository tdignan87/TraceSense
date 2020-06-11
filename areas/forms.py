from django import forms
from .models import Locations

            
class AreaForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ('code','name',)
        