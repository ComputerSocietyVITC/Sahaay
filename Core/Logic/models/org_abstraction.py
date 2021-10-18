# Setting up both organization and department models since both are similar in 
# structure and are simple in understanding

from typing_extensions import Required
from django.db import models
from Core.Logic.models.user_abstraction import UserModel

import uuid

class OrganizationModel(models.Model):
    UID = models.CharField(max_length = 9, unique = True, editable = False, null = False, blank = False, default ="default")
    Name = models.CharField(max_length=20,required = True, editable = True, null=False, blank=False, default="Orgdoe")
    prefix = models.CharField(max_length=4, editable = False, unique=True, null = False, blank = False, default="ORGD")
    type = models.CharField(max_length=15)
    
    def save(self, *args, **kwargs) -> None:
        if self.UID == "default":
            self.UID = str(uuid.uuid4().hex[:9])
            
        return super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f'{self.prefix}'
    
class DepartmentModel(models.Model):
    DepID = models.CharField(max_length = 9, unique = True, editable = False, null = False, blank = False, default ="default_DID")
    DepName = models.CharField(max_length=20,required = True, editable = True, null=False, blank=False, default="Dept_doe")
    Organization = models.ForeignKey(OrganizationModel, on_delete=models.CASCADE)
    prefix = models.CharField(max_length=4, editable = False, unique=True, null = False, blank = False, default="DEPD")
    DepDesc = models.TextField()
    Head = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs) -> None:
        if self.DepID == "default_DID":
            self.UiD = self.Organization+str(uuid.uuid4().hex[:5])
            
        return super().save(*args, **kwargs)