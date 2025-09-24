from rest_framework import serializers

from .models import Article, Commentary, Category


class CommentarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentary
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        allow_null=False
    )
    commentaries = CommentarySerializer(many=True, read_only=True, source='commentary_set')

    class Meta:
        model = Article
        fields = "__all__"
