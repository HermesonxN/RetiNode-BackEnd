from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

@api_view(['GET', 'POST'])
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

@api_view(['GET'])
def logs(request):
    logs = Logs.objects.all()
    serialized_logs = LogsSerializer(logs, many=True)
    if logs:
        return Response(serialized_logs.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def lastLog(request):
    log = Logs.objects.first()
    serialized_log = LogsSerializer(log)
    if log:
        return Response(serialized_log.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def trendingArticles(request):
    articles = Discussions.objects.filter(reads__gte=500)
    serialized_articles = DiscussionSerializer(articles, many=True)
    if articles:
        return Response(serialized_articles.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def comments(request):
    comments = Comments.objects.all()
    serialized_comment = CommentSerializer(comments, many=True)
    if comments:
        return Response(serialized_comment.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def commentators_of_the_week(request):
    commentators = Comments.objects.filter(likes__gte=500)
    serialized_commentators = CommentSerializer(commentators, many=True)
    if commentators:
        return Response(serialized_commentators.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_404_NOT_FOUND)