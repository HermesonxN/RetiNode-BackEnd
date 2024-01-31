from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DiscussionSerializer(serializers.ModelSerializer):
    userID = serializers.UUIDField(format='hex_verbose', source='user.userID')

    class Meta:
        model = Discussions
        fields = ('postID', 'userID', 'linkPost', 'date', 'title', 'description', 'image', 'likes', 'reads')