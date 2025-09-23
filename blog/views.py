from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ArticleSerializer, CommentarySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer


class CommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = CommentarySerializer

