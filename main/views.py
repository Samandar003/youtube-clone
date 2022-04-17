from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from .serializers import PlaylistSerializer, UserSerializer, VideoSerializer, CommentSerializer
from .models import User, Playlist, Video, Comment
from rest_framework.response import Response
from rest_framework import filters
from rest_framework.generics import get_object_or_404


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id', 'name', 'city', 'country', 'age', 'username']

    @action(detail=True, methods=['GET'])
    def playlist(self, request, pk):
        user = User.objects.get(id=pk)
        playlist = Playlist.objects.filter(user=user)
        serializer = PlaylistSerializer(playlist, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def video(self, request, pk):
         user = User.objects.get(id=pk)
         video = Video.objects.filter(video_user=user)
         serializer = VideoSerializer(video, many=True)
         return Response(serializer.data)

class PlaylistViewSet(ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id','playlist_name','playlist_text','playlist_date',]

    @action(detail=True, methods=['GET'])
    def get_user(self, request, pk):
        playlist = Playlist.objects.get(id=pk)
        user = playlist.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    @action(detail=True, methods=['GET'])
    def get_user(self, request, pk):
        comment = self.get_object() 
        serializer = UserSerializer(comment.user)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get_video(self, request, pk):
        comment = Comment.objects.get(id=pk)
        serializer = VideoSerializer(comment.video)
        return Response(serializer.data)


class VideoViewSet(ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [filters.SearchFilter,]
    search_fields = ['id','video_name','video_date', 'video_text',]

    @action(detail=True, methods=["GET"])
    def comments(self, request, pk):
        video = Video.objects.get(id=pk)
        comments = Comment.objects.filter(video=video)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["GET"])
    def playlists(self, request, pk):
        video = self.get_object()
        serializer = PlaylistSerializer(video.video_playlist)
        return Response(serializer.data)

    @action(detail=True, methods=['GET'])
    def get_user(self, request, pk):
        video = self.get_object() 
        serializer = UserSerializer(video.video_user)
        return Response(serializer.data)


