from django.shortcuts import render,redirect
from .forms import NewDepartment
from .models import department


def new_department(request):
    """ A view to return to the main home page """
    form = NewDepartment()
    if request.method == "POST":
        form = NewDepartment(request.POST)
    if form.is_valid():
         new_department = form.save(commit=False)
         new_department.user_id = request.user.id
         new_department.save()
         return redirect("/profile/")
    context = {'form':form}
    return render(request,"pages/new_department.html",context)
    
    


def department_list(request):
    
    departments = department.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_departments.html", {"departments":departments})

def update_department(request, pk):
    form = NewDepartment()
    context = {'form':form}
    return render(request,"pages/new_department.html",context)