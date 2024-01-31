from django.urls import path
from .views import *

urlpatterns = [
    path('users', users, name="users"),
    path('discussions/', discussions, name="discussions"),
]
