from django.shortcuts import render,redirect
from .forms import NewDepartment
from .models import department

def create_department(request):
    """create new department into the database."""
    new_department = NewDepartment()
    if request.method == "POST":
        form = NewDepartment(request.POST)
        if form.is_valid():
            createDepartment = form.save(commit=False)
            createDepartment.user_id = request.user.id
            form.save()
            return redirect("/profile")
    context = {'new_department':NewDepartment}
    return render(request,"pages/new_department.html",context)
