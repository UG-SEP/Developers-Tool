from unicodedata import name
from django.urls import path

from Home.views import Home

urlpatterns = [
    path('',Home,name="home"),
]
