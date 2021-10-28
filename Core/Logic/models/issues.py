from django.db import models
from .user_abstraction import UserModel
from multiselectfield import MultiSelectField
from .Issue_tags import DEPARTMENTS, REACTIONS, TAG_CHOICES, PRIORITY_CHOICES


class CommentsTable(models.Model):
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    Images = models.ImageField()
    Reactions = MultiSelectField(max_length=20, blank=True, choices=REACTIONS)
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE)


class Issues(models.Model):
    Issue_Name = models.CharField(max_length=200, null=False, blank=False)
    Issue_Tags = models.CharField(max_length=255, null=False, choices=TAG_CHOICES)
    Issue_description = models.TextField()
    Issue_Images = models.ImageField()
    Department = models.CharField(
        max_length=200, null=False, blank=False, choices=DEPARTMENTS
    )
    Date_of_Creation = models.DateTimeField(auto_now=True)
    Priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES)
    isActive = models.BooleanField(default=True, null=False, blank=False, editable=True)
    LinkedIssue = models.ForeignKey("self", on_delete=models.DO_NOTHING)
    User = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    Comments = models.ForeignKey(CommentsTable, on_delete=models.DO_NOTHING, default="")

    class Meta:
        verbose_name_plural = "Issues"
