from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Gmp_questions(models.Model):
    
     user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
     gmp_questionid = models.AutoField(primary_key=True)
     question = models.CharField(max_length=255, null=False, editable=True)
     created = models.DateTimeField(auto_now_add=True, null=False, editable=False)
     def __str__(self):
            return self.question