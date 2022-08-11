from rest_framework.viewsets import ViewSet
from personalwebsiteapi.models.formmodel import FormModel
from personalwebsiteapi.models.formskill import FormSkillModel
from personalwebsiteapi.models.industrymodel import IndustryModel
from personalwebsiteapi.models.membermodel import MemberModel
from personalwebsiteapi.models.skillmodel import SkillModel
from personalwebsiteapi.serializers.form_serializer import FormSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
import django_on_heroku

class FormViews (ViewSet):
    
    def list(self, request):
        forms = FormModel.objects.all()
        
        serializer = FormSerializer(forms, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    
    def create(self, request):

        skill_list = []
        for key in request.data["skills"]:
            if request.data['skills'][key] is True:
              
                skill = SkillModel.objects.get(name = key)
                skill_list.append(skill.pk)
                
            
        

        
        
        serializer = FormSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        form = FormModel.objects.get(pk = serializer.data['id'])
        form.skills.add(*skill_list)
            
        
        serializer = FormSerializer(form)
        
        return Response(data = serializer.data, status = status.HTTP_201_CREATED)
        
        