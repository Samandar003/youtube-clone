from django.urls import include, path
from .models import *
from . import views
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet, PlaylistViewSet, CommentViewSet,
    VideoViewSet
)

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('playlists', PlaylistViewSet)
router.register('comments', CommentViewSet)
router.register('videos', VideoViewSet)

urlpatterns = [
    path('', include(router.urls))
]

