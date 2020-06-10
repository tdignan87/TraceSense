from django.shortcuts import render,redirect, get_object_or_404
from .forms import AreaForm
from .models import Areas

def create_area(request):
    """ Function for creating a new area in the database."""
    Areaform = AreaForm()
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            createArea = form.save(commit=False)
            createArea.user_id = request.user.id
            form.save()
            return redirect("/profile")
    context = {'form':AreaForm}
    return render(request,"pages/new_area.html",context)

def area_list(request):
    area = Areas.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_areas.html",{"areas":area})

def update_area(request, pk):
    area = Areas.objects.get(id=pk)
    form = AreaForm(instance=area)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect("/profile")
    context = {'form':form}
    return render(request,"pages/new_area.html",context)

def delete_area(request, pk):
    area = Areas.objects.get(id=pk)
    if request.method == "POST":
        area.delete()
        return redirect("/profile")
    
    context = {'name':area,
               'code':area,}
    return render(request, 'pages/delete_area.html',context)
