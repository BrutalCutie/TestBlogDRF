from rest_framework import serializers

from .models import Article, Commentary, Category


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=False
    )

    class Meta:
        model = Article
        fields = "__all__"


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = "__all__"
