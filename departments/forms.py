from django import forms
from .models import  department

class NewDepartment(forms.ModelForm):
    class Meta:
        model = department
        fields = ('department',)