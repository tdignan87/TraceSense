from django.db import models
from django.contrib.auth.models import User
from areas.models import Locations
from questions.models import Gmp_questions

class Transactions(models.Model):
    
    audit_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    location_id = models.ForeignKey(Locations,null=False,on_delete=models.DO_NOTHING)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    gmp_questionid = models.ForeignKey(Gmp_questions,null=False,on_delete=models.DO_NOTHING)
    compliant = models.SmallIntegerField(null=True,editable=True)
    fail = models.SmallIntegerField(null=True,editable=True)
    freetext = models.CharField(max_length=255,null=True,editable=True)
    status = models.BooleanField(default=False)