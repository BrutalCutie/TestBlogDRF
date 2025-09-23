from rest_framework import serializers

from .models import Article, Commentary


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = "__all__"
