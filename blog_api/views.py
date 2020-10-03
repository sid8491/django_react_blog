from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters

class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


class PostList(generics.ListAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = PostSerializer

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=item)

    # Define Custom Queryset
    # def get_queryset(self):
    #     return Post.objects.all()

    # to get posts by user
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter()

# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
#     queryset = Post.post_objects.all()
#     serializer_class = PostSerializer


class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        slug = self.kwargs.get('slug')
        # user = self.request.user
        # queryset = Post.objects.filter(slug=slug, author=user)
        queryset = Post.objects.filter(slug=slug)
        return queryset

class PostSearch(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$slug']