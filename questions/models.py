from django.db import models
from django.contrib.auth.models import User

# Create your models here.


def __str__(self):
    return self.name


class Gmp_questions(models.Model):
    
     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     gmp_questionid = models.AutoField(primary_key=True)
     question = models.CharField(max_length=255, null=False, editable=True)
     created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
     
    
class Gmp_answers(models.Model):
    
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    gmp_id = models.AutoField(primary_key=True)
    gmp_questionid = Gmp_questions.gmp_questionid
    compliant = models.SmallIntegerField(null=True,editable=True)
    fail = models.SmallIntegerField(null=True,editable=True)
    freetext = models.CharField(max_length=255,null=True,editable=True)