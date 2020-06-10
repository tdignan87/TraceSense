from django.contrib import admin
from .models import Areas

class SiteAreas(admin.ModelAdmin):
    
    readonly_fields = ('id','created',)
    
    fields = ('code','name','created_by',)
    
    list_display = ('id', 'code','name',)

admin.site.register(Areas, SiteAreas)