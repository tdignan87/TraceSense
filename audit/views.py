from django.shortcuts import render,redirect
from .models import Gmp_questions,Transactions,Locations
from .forms import AuditTransaction



def new_audit(request):
    """ Create new audit and store into the database."""
    auditForm = AuditTransaction()
    my_questions = Gmp_questions.objects.filter(user=request.user)
    my_locations = Locations.objects.filter(user=request.user)
    if request.method == "POST":
        auditForm(request.POST)
        if auditForm.is_valid():
            createAudit = auditForm.save(commit=False)
            createAudit.user_id = request.user.id
            auditForm.save()
            return render(request,"pages/view_audits.html")
    context = {'form':auditForm,
               'question':my_questions,
               'location':my_locations}
    return render(request,"pages/new_audit.html",context)
