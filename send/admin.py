from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    
    readonly_fields = ('contact_id','created',)
    
    fields = ('contact_name','contact_email','enquiry_details',)
    
    list_display = ('contact_name', 'contact_email','enquiry_details',)

admin.site.register(ContactForm, ContactFormAdmin)
