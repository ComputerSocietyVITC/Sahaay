from django.db import models
from pathlib import Path
from .user_abstraction import UserModel
from multiselectfield import MultiSelectField
from .options import DEPARTMENTS, REACTIONS, TAG_CHOICES, PRIORITY_CHOICES, read_file

DIR = str(Path(__file__).resolve().parent.parent) + r"/models/fixtures"

class CommentsTable(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Images = models.ImageField()
    Reactions = MultiSelectField(max_length=20, blank=True, choices=read_file(DIR + str(Path('/rxn.json'))))
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE, null = True)


class Issues(models.Model):
    Issue_Name = models.CharField(max_length=200, null=False, blank=False)
    Issue_Tags = models.CharField(max_length=255, null=False, choices=read_file(DIR + '/choices.json'))
    Issue_description = models.TextField()
    Issue_Images = models.ImageField()
    Department = models.CharField(
        max_length=200, null=False, blank=True, choices=DEPARTMENTS, default = "Admin"
    )
    Date_of_Creation = models.DateTimeField(auto_now=True)
    Priority = models.CharField(max_length=100, choices=read_file(DIR + '/priority.json'))
    isActive = models.BooleanField(default=True, null=False, blank=True, editable=True)
    LinkedIssue = models.ForeignKey("self", on_delete=models.DO_NOTHING, null = True, blank=True)
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Comments = models.ForeignKey(CommentsTable, on_delete=models.DO_NOTHING, default="", null = True, blank=True)

    class Meta:
        verbose_name_plural = "Issues"

