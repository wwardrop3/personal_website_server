from django.db import models


class FormSkillModel (models.Model):
    form = models.ForeignKey('FormModel', on_delete=models.CASCADE)
    skill = models.ForeignKey('SkillModel', on_delete=models.CASCADE)
