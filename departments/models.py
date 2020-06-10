from django.db import models
from django.contrib.auth.models import User

class Department(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    department_id = models.AutoField(primary_key=True)
    department = models.CharField(max_length=50,null=False,editable=True)
    created = models.DateTimeField(auto_now_add=True, null=False, editable=False)

    def __str__(self):
        return self.department