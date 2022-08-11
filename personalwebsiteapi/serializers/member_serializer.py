from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

from personalwebsiteapi.models.membermodel import MemberModel
from personalwebsiteapi.serializers.user_serializer import UserSerializer

class MemberSerializer(ModelSerializer):
    
    
    user = UserSerializer()
    
    
    class Meta:
        model = MemberModel
        fields = ("id", "bio", "user")
        depth = 1