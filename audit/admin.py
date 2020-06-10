from django.contrib import admin
from .models import gmp_questions

class GMPQuestionAdmin(admin.ModelAdmin):
    
    readonly_fields = ('gmp_questionid','created','user_id',)
    
    fields = ('question',)
    
    list_display = ('gmp_questionid', 'created', 'question')
    
    
admin.site.register(gmp_questions, GMPQuestionAdmin)
