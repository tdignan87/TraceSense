from django import forms
from .models import Transactions
from django.contrib.auth.models import User

class AuditTransaction(forms.ModelForm):
    class Meta:
        model = Transactions
        
        readonly_fields = ('created',)
        
        fields = ('location','gmp_question','compliant','freetext','status')
       
        compliant_choices = [1,2]
        
        widgets = {
            
            'location':forms.Select(attrs={"class": "form-control required"}), 
            'gmp_question': forms.Select(attrs={"class": "form-control required"}),
            'status': forms.Select(attrs={"class": "form-control required"}),
            'freetext': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.TextInput(attrs={"class": "form-control"}),      
        
            }
      
  