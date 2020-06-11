from django.contrib import admin
from .models import Locations

class SiteAreas(admin.ModelAdmin):
    
    readonly_fields = ('location_id','created',)
    
    fields = ('code','name','created_by',)
    
    list_display = ('location_id', 'code','name',)

admin.site.register(Locations, SiteAreas)