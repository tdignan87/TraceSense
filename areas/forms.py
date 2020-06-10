from django import forms
from .models import Areas

            
class AreaForm(forms.ModelForm):
    class Meta:
        model = Areas
        fields = ('code','name',)
        