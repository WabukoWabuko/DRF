from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.decorators import APIView, api_view
from rest_framework.views import status
from rest_framework.views import APIView
from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]
  