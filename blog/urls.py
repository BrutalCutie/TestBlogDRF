from django.urls import path
from rest_framework.routers import DefaultRouter

from blog.apps import BlogConfig
from . import views
app_name = BlogConfig.name

router = DefaultRouter()

router.register('articles', viewset=views.ArticleViewSet, basename='articles')
router.register('commentaries', viewset=views.CommentaryViewSet, basename='commentaries')

urlpatterns = [

] + router.urls
