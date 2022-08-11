from django.db import models
from django.contrib.auth.models import User


class MemberModel (models.Model):
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)