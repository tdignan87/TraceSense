from django import forms
from .models import ContactForm

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
    
        fields = ['contact_name','contact_email','enquiry_details',]
        
        widgets =  {
            'contact_name': forms.TextInput(attrs={"class": "form-control"}),
            'contact_email': forms.EmailInput(attrs={"class": "form-control",}),
            'enquiry_details': forms.TextInput(attrs={"class": "form-control"}),
        }
        
        
        