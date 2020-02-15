from rest_framework import serializers
from contact_rest_api import models

class UserProfileSerializer(serializers.ModelSerializer):
   """Serializes a profile object"""

   class Meta:
       model = models.UserProfile
       fields = ("id", "email", "name", "password")
       extra_kwargs={
           "password":{
               "write_only":True,
               "style":{
                   "input_type":"password"
               }
           }
       }

   def create(self, validated_data):
       """Create and return new user"""
       user = models.UserProfile.objects.create_user(
           email=validated_data["email"],
           name=validated_data["password"],
           password=validated_data["password"]
       )
       return user

class ContactSerializer(serializers.ModelSerializer):
    """Serializer for contact """
    class Meta:
        model = models.Contact
        fields=("id", "name", "phone", "address")