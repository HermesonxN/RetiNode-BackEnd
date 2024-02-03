from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class DiscussionSerializer(serializers.ModelSerializer):
    userName = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True, source='user.name');

    class Meta:
        model = Discussions
        fields = ('postID', 'userName', 'linkPost', 'date', 'title', 'description', 'image', 'likes', 'reads')

class LogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logs
        fields = '__all__'