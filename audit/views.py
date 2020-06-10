from django.shortcuts import render,redirect, get_object_or_404
from .forms import AreaForm
from .models import areas

def create_area(request):
    Areaform = AreaForm()
    if request.method == "POST":
        form = AreaForm(request.POST)
        if form.is_valid():
            createArea = form.save(commit=False)
            createArea.user_id = request.user.id
            form.save()
            return redirect("/profile")
    context = {'Areaform':AreaForm}
    return render(request,"pages/areas.html",context)

def area_list(request):
    area = areas.objects.filter(user_id=request.user.id)
    return render(request,"pages/view_areas.html",{"area":area})

def update_area(request, pk):
    
    area = areas.objects.get(id=pk)
    form = AreaForm(instance=area)
    if request.method == "POST":
        form = AreaForm(request.POST, instance=area)
        if form.is_valid():
            form.save()
            return redirect("/profile")
    context = {'Areaform':AreaForm}
    return render(request,"pages/areas.html",context)

def delete_area(request, pk):
    area = areas.objects.get(id=pk)
    if request.method == "POST":
        area.delete()
        return redirect("/profile")
    
    context = {'name':area,
               'code':area,}
    return render(request, 'components/delete.html',context)



    

  
        
            
    