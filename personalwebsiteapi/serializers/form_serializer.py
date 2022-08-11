

from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from personalwebsiteapi.models.formmodel import FormModel
from personalwebsiteapi.serializers.member_serializer import MemberSerializer
from personalwebsiteapi.serializers.skill_serializer import SkillSerializer
from personalwebsiteapi.serializers.user_serializer import UserSerializer

class FormSerializer(ModelSerializer):
    

    
    class Meta:
        model = FormModel
        fields = ("id", "first_name", "email", "last_name", "company", "ok_to_contact", "hiring", "skills" )
        depth = 1
        
        

class CreateFormSerializer(ModelSerializer):
    
    skills = SkillSerializer(many = True)
    
    class Meta:
        model = FormModel
        fields = ("id", "first_name", "email", "last_name", "company", "ok_to_contact", "hiring", "skills" )