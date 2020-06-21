from django.db import models
from django.contrib.auth.models import User
from areas.models import Locations
from questions.models import Gmp_questions

class Transactions(models.Model):
    class Meta:
        verbose_name_plural = "transactions"
    
    audit_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    location = models.ForeignKey(Locations,null=False,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    gmp_question = models.ForeignKey(Gmp_questions,null=False,on_delete=models.DO_NOTHING,related_name='gmp_questions')
    compliant = models.BooleanField("Is Compliant?/No Risk",default=False)
    freetext = models.CharField(max_length=255,null=True,editable=True)
    
    statusChoice =(('Open','Open'),
        ('Closed','Closed'))
    
    status = models.CharField(max_length=6,choices=statusChoice,null=False,editable=True)
    
    