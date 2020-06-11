from django.shortcuts import render,redirect
from .forms import NewDepartment
from .models import Department

def create_department(request):
    """create new department into the database."""
    new_department = NewDepartment()
    if request.method == "POST":
        form = NewDepartment(request.POST)
        if form.is_valid():
            createDepartment = form.save(commit=False)
            createDepartment.user_id = request.user.id
            form.save()
            return redirect(department_list)
    context = {'form':NewDepartment}
    return render(request,"pages/new_department.html",context)


def department_list(request):
    """ function for rendering department list from model"""
    dep = Department.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_departments.html",{"department":dep})

def update_department(request,pk):
    """ function for updating the department values"""
    dep = Department.objects.get(department_id=pk)
    form = NewDepartment(instance=dep)
    if request.method =="POST":
        dep = NewDepartment(request.POST, instance=dep)
        if form.is_valid():
            form.save()
            return redirect(department_list)
    context = {'form':form}
    return render(request,"pages/new_department.html",context)

def delete_department(request,pk):
    """ function for deleting department from database. """
    dep = Department.objects.get(department_id=pk)
    if request.method == "POST":
        dep.delete()
        return redirect(department_list)
    
    context={'department':dep}
    return render(request,"pages/delete_department.html",context)


