from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions, generics, pagination,viewsets
from blog.models import Post
from blog.api.serializer import PostSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]