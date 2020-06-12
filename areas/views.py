from django.shortcuts import render,redirect, get_object_or_404
from .forms import AreaForm
from .models import Locations

def create_area(request):
    """ Function for creating a new area in the database."""
    Areaform = AreaForm()
    form_class = AreaForm
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            createArea = form.save(commit=False)
            createArea.user_id = request.user.id
            form.save()
            return redirect(area_list)
    context = {'form':AreaForm}
    return render(request,"pages/new_area.html",context)

def area_list(request):
    area = Locations.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_areas.html",{"areas":area})

def update_area(request, pk):
    area = Locations.objects.get(location_id=pk)
    form = AreaForm(instance=area)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect(area_list)
    context = {'form':form}
    return render(request,"pages/new_area.html",context)

def delete_area(request, pk):
    area = Locations.objects.get(location_id=pk)
    if request.method == "POST":
        area.delete()
        return redirect(area_list)
    
    context = {'name':area,
               'code':area,}
    return render(request, 'pages/delete_area.html',context)
