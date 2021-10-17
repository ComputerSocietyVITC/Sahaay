from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser): 
    Reg_no = models.CharField(max_length = 9, editable = True, null = False, blank = False, default = '00VIT----')