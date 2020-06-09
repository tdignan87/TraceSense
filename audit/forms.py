from django import forms
from .models import gmp_questions, department, areas

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = gmp_questions
        fields = ('question',) 
        
        
class NewDepartment(forms.ModelForm):
    class Meta:
        model = department
        fields = ('department',)
        
class AreaForm(forms.ModelForm):
    class Meta:
        model = areas
        fields = ('code','name',)
        