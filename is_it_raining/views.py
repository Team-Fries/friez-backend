from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, filters

from .models import User


@api_view(["GET"])
def api_root(request, format=None):
    return Response()
