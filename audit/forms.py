from django import forms
from .models import gmp_questions, department

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = gmp_questions
        fields = ('question',) 
        
        
class NewDepartment(forms.ModelForm):
    class Meta:
        model = department
        fields = ('department',)
        readonly_fields = ('user',)
    