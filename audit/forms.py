from django import forms
from .models import gmp_questions

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = gmp_questions
        fields = ('question',) 
        
            

        