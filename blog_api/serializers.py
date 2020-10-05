from rest_framework import serializers
from blog.models import Post
from users.models import CustomUser

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author', 'excerpt', 'content', 'status')

class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}