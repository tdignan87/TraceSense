from django import forms
from .models import  Department

class NewDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields = ('department',)
        
        widgets = {
            'department': forms.TextInput(attrs={"class": "form-control"})
        }