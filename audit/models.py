from django.db import models

# Create your models here.

class gmp_questions(models.Model):
    
     gmp_questionid = models.AutoField(primary_key=True)
     question = models.CharField(max_length=255, null=False, editable=True)
     created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
     created_by = models.CharField(max_length=30, null=True, editable=True)
     
    
     
class area(models.Model):
    
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5,null=False,editable=True)
    name = models.CharField(max_length=255,null=False,editable=True)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    created_by = models.CharField(max_length=30, null=False, editable=True)
    
    
class department(models.Model):
    
    department_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50,null=False,editable=True)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
    created_by = models.CharField(max_length=30, null=False, editable=True)
    
class gmp_answers(models.Model):
    gmp_id = models.AutoField(primary_key=True)
    gmp_questionid = gmp_questions.gmp_questionid
    compliant = models.SmallIntegerField(null=True,editable=True)
    fail = models.SmallIntegerField(null=True,editable=True)
    freetext = models.CharField(max_length=255,null=True,editable=True)