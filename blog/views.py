from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .permissions import IsOwner
from .serializers import ArticleSerializer, CommentarySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Article.objects.prefetch_related("commentary_set").all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update'):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()


class CommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = CommentarySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        article_obj = get_object_or_404(Article, pk=self.request.data.get("article"))
        serializer.save(author=self.request.user, article=article_obj)

    def get_permissions(self):
        if self.action in ('destroy', 'update', 'partial_update'):
            self.permission_classes = [IsAuthenticated, IsOwner]
        return super().get_permissions()

