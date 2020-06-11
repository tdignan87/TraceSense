from django import forms
from .models import Transactions

class AuditTransaction(forms.ModelForm):
    class Meta:
        model = Transactions
        
        readonly_fields = ('created',)
        
        fields = ('compliant','fail','freetext','status')
        
        
        