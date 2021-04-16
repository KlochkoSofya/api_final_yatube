from .models import Post, Group
from .serializers import PostSerializer, CommentSerializer
from .serializers import FollowSerializer, GroupSerializer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from rest_framework import permissions
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group', ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,
    ]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__username', 'following__username']
    http_method_names = ['get', 'post']

    def get_queryset(self):
        return self.request.user.following

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [
        IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly,
    ]
    http_method_names = ['get', 'post']
