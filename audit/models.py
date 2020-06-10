from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def __str__(self):
    return self.name


class gmp_questions(models.Model):
    
     user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
     gmp_questionid = models.AutoField(primary_key=True)
     question = models.CharField(max_length=255, null=False, editable=True)
     created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
     
    
class gmp_answers(models.Model):
    
    gmp_id = models.AutoField(primary_key=True)
    gmp_questionid = gmp_questions.gmp_questionid
    compliant = models.SmallIntegerField(null=True,editable=True)
    fail = models.SmallIntegerField(null=True,editable=True)
    freetext = models.CharField(max_length=255,null=True,editable=True)