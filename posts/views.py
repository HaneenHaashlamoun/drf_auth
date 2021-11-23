from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializer import PostSerializer

# Create your views here.

class PostList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)    
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)    
    queryset = Post.objects.all()
    serializer_class = PostSerializer