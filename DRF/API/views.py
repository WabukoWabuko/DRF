from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.decorators import api_view
from rest_framework.views import status


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

  if request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
  try:
    article = Article.objects.all(pk=pk)
  except Article.DoesNotExist:
    return Response({'error': 'Article Not Found'}, status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

  if request.method == 'PUT':
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)