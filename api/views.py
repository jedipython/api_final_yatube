from rest_framework import viewsets
from .serializers import PostSerializer, CommentSerializer, FollowSerializer, GroupSerializer
from .models import Post, Comment, Follow, Group
from .permissions import IsAuthorOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['group',]

    def perform_create(self, serializer):
        # переопределяем  save() при создании и создаем пост
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]


    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self, **kwargs):
        post = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthorOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=user__username', '=following__username',] #поиск по точным совпадениям

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthorOrReadOnly]
    
