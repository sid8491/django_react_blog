from blog.models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView

# class PostUserWritePermission(permissions.BasePermission):
#     message = 'Editing posts is restricted to author only.'

#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return obj.author == request.user

# display all posts
class PostList(generics.ListAPIView):
    # permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    # custom queryset to get posts by user
    # def get_queryset(self):
    #     user = self.request.user
    #     return Post.objects.filter()

# detail about single post
class PostDetail(generics.ListAPIView):
    serializer_class = PostSerializer

    # def get_object(self, queryset=None, **kwargs):
    #     item = self.kwargs.get('pk')
    #     return get_object_or_404(Post, slug=id)

    def get_queryset(self):
        slug = self.request.query_params.get('slug', None)
        slug = self.kwargs.get('slug')
        # user = self.request.user
        # queryset = Post.objects.filter(slug=slug, author=user)
        queryset = Post.objects.filter(slug=slug)
        return queryset

# superarch and show posts
class PostSearch(generics.ListAPIView):
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['$slug']

# post admin
class CreatePost(generics.CreateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class AdminPostDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class EditPost(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer