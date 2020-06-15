from django.shortcuts import render,redirect
from django.core.mail import send_mail
from .forms import ContactUsForm
from tracesense.settings import EMAIL_HOST_USER

def send_form(request):
    """ Form for sending email enquiry into tracesense. Exception if SMTP fails """
    sendform = ContactUsForm()
    form_class = ContactUsForm
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(confirm_mail)
    context = {'form':ContactUsForm}
    return render(request,"pages/contact-form.html",context)

def confirm_mail(request):
    """ try and send email - if fails return error page. Automatic email to company, who then can follow up enquiry."""
    try:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            contact_name = form.cleaned_data['contact_name']
            contact_email = form.cleaned_data['contact_email']
            contact_message = form.cleaned_data['contact_message']
           
        send_mail(
        'Contact Form Enquiry',
        'A new enquiry is in the system. Please check the system to review.',
        EMAIL_HOST_USER,
        ['tom.dignan@tracesense.co.uk'],
        fail_silently=False,
        )
        return render(request,"pages/confirmation.html")
    except:
        return render(request,"pages/error-form.html")


