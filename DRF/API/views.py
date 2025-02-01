from django.shortcuts import render
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.decorators import APIView, api_view
from rest_framework.views import status
from rest_framework.views import APIView


# Create your views here.
class ArticleListAPIView(APIView):

  def get(self, request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      # print("Saved Data", serializer.data) # For debugging
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    # print("Errors", serializer.errors) # for debugging
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetailAPIView(APIView):

  def get_object(self, pk):
    try:
      article = Article.objects.all(pk=pk)
    except Article.DoesNotExist:
      return Response({'error': 'Article Not Found'},
                      status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
      if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
      if request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
      if request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
