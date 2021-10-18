from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

class UserModel(AbstractUser):
    Reg_no = models.CharField(
        max_length=9,
        unique=True,
        editable=True,
        null=False,
        blank=False,
        default="00VIT----",
    )
    UiD = models.CharField(
        max_length=255,
        unique=True,
        editable=False,
        null=False,
        blank=False,
        default=uuid.uuid4,
    )