from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer


class UserListCreateView(ListCreateAPIView):
    """
    API endpoint for listing all users or creating a new user.
    
    GET /posts/users/ - List all users
    POST /posts/users/ - Create a new user (requires: username, email)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PostListCreateView(ListCreateAPIView):
    """
    API endpoint for listing all posts or creating a new post.
    
    GET /posts/posts/ - List all posts with author metadata
    POST /posts/posts/ - Create a new post (requires: content, author)
    """
    queryset = Post.objects.select_related('author').prefetch_related('comments').all()
    serializer_class = PostSerializer


class CommentListCreateView(ListCreateAPIView):
    """
    API endpoint for listing all comments or creating a new comment.
    
    GET /posts/comments/ - List all comments across all posts
    POST /posts/comments/ - Create a comment (requires: text, post, author)
    """
    queryset = Comment.objects.select_related('author', 'post').all()
    serializer_class = CommentSerializer

