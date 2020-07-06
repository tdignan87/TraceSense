from django.shortcuts import render,redirect
from .models import Gmp_questions,Transactions,Locations
from checkout.models import Order
from .forms import AuditTransaction



def new_audit(request):
    """ Create new audit and store into the database."""
    auditForm = AuditTransaction()
    my_questions = Gmp_questions.objects.filter(user_id=request.user.id)
    my_locations = Locations.objects.filter(user_id=request.user.id)
    gmp_data_audit = Transactions.objects.filter(user_id=request.user.id)
    if request.method == "POST":
        form = AuditTransaction(request.POST)
        if form.is_valid():
            createAudit = form.save(commit=False)
            createAudit.user_id = request.user.id
            form.save()
            return redirect(audit_list)
    context = {'form':auditForm,
               'question':my_questions,
               'location':my_locations}
    return render(request,"pages/new_audit.html",context)


def audit_list(request):
    """ Show list of audit items """
    audit_data = Transactions.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_audits.html",{"data":audit_data})

def update_audit(request,pk):
    """ function for updating audits values values"""
    audit = Transactions.objects.get(audit_id=pk)
    form = AuditTransaction(instance=audit)
    if request.method =="POST":
        form = AuditTransaction(request.POST, instance=audit)
        if form.is_valid():
            form.save()
            return redirect(audit_list)
    context = {'form':form}
    return render(request,"pages/new_audit.html",context)

def delete_audit(request,pk):
    """ function for deleting audit from database """
    audit = Transactions.objects.get(audit_id=pk)
    if request.method == "POST":
        audit.delete()
        return redirect(audit_list)
    
    context={'audit':audit}
    return render(request,"pages/delete_audits.html",context)

def open_actions(request):
    """Show list of open audit items"""
    myOrder = Order.objects.filter(user_id=request.user.id)
    audit_actions = Transactions.objects.filter(user_id=request.user.id,
                                                status="Open",
                                                )
    context={'orders':myOrder}
    return render(request,"pages/open_actions.html",{"data":audit_actions,
                                                     "orders":myOrder})
    

def completed_actions(request):
    """Show list of completed audit action items"""
    myOrder = Order.objects.filter(user_id=request.user.id)
    audits_completed = Transactions.objects.filter(user_id=request.user.id,
                                                    status="Closed")
    context={'orders':myOrder}
    return render(request,"pages/completed.html",{"data":audits_completed,
                                                  "orders":myOrder})