from django import forms
from .models import gmp_question

class GMPQuestions(forms.ModelForm):
    class Meta:
        model = gmp_question
        fields = ('question','deleted',)