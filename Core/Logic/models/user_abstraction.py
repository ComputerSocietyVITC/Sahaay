from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class UserModel(AbstractUser): 
    Reg_no = models.CharField(max_length = 9, unique = True, editable = True, null = False, blank = False, default = '00VIT----')
    UiD = models.CharField(max_length = 9, unique = True, editable = False, null = False, blank = False, default ='defo12345')
    
    def save(self, reg_edited=False, *args, **kwargs) -> None:
        # Code to ensure a new UiD is generated when first user is created
        # Only the reg_no prefix gets updated if only Reg_no is updated
        # To be changed if better logic can be found
        
        uid = self.UiD
        if uid == 'defo12345' or reg_edited == True:
            reg_no = self.Reg_no
            self.UiD = reg_no[:4]+ ( str(uuid.uuid4().hex[:5]) if reg_edited == False else  self.UiD[-5:])
        
        return super().save(*args, **kwargs)
        