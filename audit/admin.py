from django.contrib import admin
from .models import gmp_questions, area, department

class GMPQuestionAdmin(admin.ModelAdmin):
    
    readonly_fields = ('gmp_questionid','created',)
    
    fields = ('question',)
    
    list_display = ('gmp_questionid', 'created', 'question',)
    
    
admin.site.register(gmp_questions, GMPQuestionAdmin)


class SiteAreas(admin.ModelAdmin):
    
    readonly_fields = ('id','created',)
    
    fields = ('code','name','created_by',)
    
    list_display = ('id', 'code','name', 'created_by',)

admin.site.register(area, SiteAreas)

class Departments(admin.ModelAdmin):
    
    readonly_fields = ('department_id','created',)
    
    fields = ('department','created_by',)
    
    list_display = ('department_id', 'created','department', 'created_by',)
    
admin.site.register(department,Departments)