from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated

from .serializers import ArticleSerializer, CommentarySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]


class CommentaryViewSet(viewsets.ModelViewSet):
    serializer_class = CommentarySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        commentary = serializer.save()
        commentary.author = self.request.user
        commentary.article = self.kwargs.get("pk")
        commentary.save()

