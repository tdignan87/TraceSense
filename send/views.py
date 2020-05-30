from django.shortcuts import render
from django.core.mail import send_mail

def send_form(request):
    
    send_mail (
        'Test Mail',
        'This is just a email test',
        'info@tracesense.co.uk',
        ['tom.dignan@tracesense.co.uk'],
         fail_silently=False,
    )
    return render(request,"pages/support.html")
