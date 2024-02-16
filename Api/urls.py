from django.urls import path
from .views import *

urlpatterns = [
    path('users/', users, name="users"),
    path('discussions/', discussions, name="discussions"),
    path('logs/', logs, name="logs"),
    path('last-log/', lastLog, name="last-log"),
    path('trending-articles/', trendingArticles, name="trending-articles"),
    path('comments/', comments, name="comments"),
    path('commentators-of-the-week/', commentators_of_the_week, name="commentators_of_the_week")
]
