from django.contrib import admin
from .models import UserModel, CommentsTable

admin.site.register([UserModel, CommentsTable])
