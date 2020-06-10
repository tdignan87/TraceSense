from django.contrib import admin
from .models import gmp_questions, areas

class GMPQuestionAdmin(admin.ModelAdmin):
    
    readonly_fields = ('gmp_questionid','created','user_id',)
    
    fields = ('question',)
    
    list_display = ('gmp_questionid', 'created', 'question')
    
    
admin.site.register(gmp_questions, GMPQuestionAdmin)


class SiteAreas(admin.ModelAdmin):
    
    readonly_fields = ('id','created',)
    
    fields = ('code','name','created_by',)
    
    list_display = ('id', 'code','name',)

admin.site.register(areas, SiteAreas)