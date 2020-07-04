from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name','email','phone_number',
                  'street_address',
                  'town_or_city','postcode','country',)
        
        readonly_fields = ('grand_total',)
        widgets = {
            
            'full_name':forms.TextInput(attrs={"class": "form-control required"}), 
            'email': forms.EmailInput(attrs={"class": "form-control required"}),
            'phone_number': forms.TextInput(attrs={"class": "form-control required"}),
            'country': forms.TextInput(attrs={"class": "form-control"}),
            'postcode': forms.TextInput(attrs={"class": "form-control"}),      
            'town_or_city': forms.TextInput(attrs={"class": "form-control"}), 
            'street_address': forms.TextInput(attrs={"class": "form-control"}), 
        }
        
        
def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address': 'Street Address',
        }
      

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            
            
      