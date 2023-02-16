from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from API.apiviews import SumIntegers

urlpatterns = [
    path("add/", SumIntegers.as_view()),
]
