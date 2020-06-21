from django import forms
from .models import Transactions

class AuditTransaction(forms.ModelForm):
    class Meta:
        model = Transactions
        
        readonly_fields = ('created',)
        
        fields = ('compliant','freetext','status')
       
        compliant_choices = [1,2]
        
        widgets = {
            'status': forms.Select(attrs={"class": "form-control required"}),
            'freetext': forms.TextInput(attrs={"class": "form-control"}),
            'body': forms.TextInput(attrs={"class": "form-control"})      }
      