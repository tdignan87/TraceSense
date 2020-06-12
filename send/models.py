from django.db import models

class ContactForm(models.Model):
    
    contact_id = models.AutoField(primary_key=True)
    contact_name = models.CharField(max_length=55,null=False,editable=True)
    contact_email = models.EmailField(max_length=55,null=False,editable=True)
    enquiry_details = models.CharField(max_length=255,null=False,editable=True)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    
