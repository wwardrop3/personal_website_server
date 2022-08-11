from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from personalwebsiteapi.models.skillmodel import SkillModel

class SkillSerializer(ModelSerializer):
    
    class Meta:
        model = SkillModel
        fields = ("id", "name")