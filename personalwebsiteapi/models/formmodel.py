
from django.db import models
from django.contrib.auth.models import User

from personalwebsiteapi.models.membermodel import MemberModel

class FormModel (models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.TextField()
    company = models.TextField()
    ok_to_contact = models.BooleanField(null=False)
    # member = models.ForeignKey("MemberModel", on_delete=models.CASCADE)
    hiring = models.BooleanField(null=False)
    skills = models.ManyToManyField("SkillModel", through="FormSkillModel", related_name="form")


