from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer, CommentarySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = CommentarySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        article_obj = get_object_or_404(Article, pk=self.kwargs.get("pk"))
        serializer.save(author=self.request.user, article=article_obj)
