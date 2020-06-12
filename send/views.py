from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactUsForm

def send_form(request):
    """ Form for sending email enquiry into tracesense. Exception if SMTP fails """
    sendform = ContactUsForm()
    form_class = ContactUsForm
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if sendform.is_valid():
            form.save()
            try:
                send_data()
                return render(request,"pages/confirmation.html")
            except:
                render(request,"pages/error-form.html")
        return render(request,"pages/confirmation.html")
            
    context = {'form':ContactUsForm}
    return render(request,"pages/contact-form.html",context)

def confirm_mail(request):
    return render(request,"pages/confirmation.html")

def send_data(request):
    form = ContactUsForm()
    contact_name = form.cleaned_data['contact_name']
    contact_email = form.cleaned_data['contact_email']
    enquiry_details = form.cleaned_data['enquiry_details']
    send_mail()
    
    send_mail (
        'Contact Form Enquiry',
        enquiry_details,
        contact_email,
        ['tom.dignan@tracesense.co.uk'],
         fail_silently=False,
        )
  