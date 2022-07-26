from rest_framework import serializers,mixins

from .models import Notes



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notes
        fields=['id','title','content']


# class UserSerializer(serializers.Serializer):
#     class Meta:
#         model=Users
#         fields=['id','username','email','password']

