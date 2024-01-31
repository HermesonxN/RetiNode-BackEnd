from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET'])
def discussions(request):
    discussions = Discussions.objects.all()
    serialized_discussions = DiscussionSerializer(discussions, many=True)
    if discussions:
        return Response(serialized_discussions.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def users(request):
    users = User.objects.all()
    serialized_users = UserSerializer(users, many=True)
    if users:
        return Response(serialized_users.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)