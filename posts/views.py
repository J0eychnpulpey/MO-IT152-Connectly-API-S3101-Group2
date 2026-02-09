from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import User, Post, Comment
from .serializers import UserSerializer, PostSerializer, CommentSerializer
from .permissions import IsPostAuthor, IsCommentAuthor

from factories.postfactory import PostFactory
from singletons.loggersingleton import LoggerSingleton

# initialize the logger singleton
logger = LoggerSingleton().get_logger()

class UserListCreateView(ListCreateAPIView):
    """
    API endpoint for listing all users or creating a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PostListCreateView(APIView):
    """
    API endpoint for listing all posts or creating a new post using the Factory pattern.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        author_id = data.get('author')
        
        try:
            author = User.objects.get(id=author_id)
            # use the factory to create the post
            post = PostFactory.create_post(
                post_type=data.get('post_type', 'text'),
                title=data.get('title', 'Untitled'),
                content=data.get('content', ''),
                author=author,
                metadata=data.get('metadata')
            )
            logger.info(f"Post created successfully: {post.id}")
            return Response({"message": "Post created successfully!", "id": post.id}, status=status.HTTP_201_CREATED)
        
        except User.DoesNotExist:
            logger.error(f"User with id {author_id} not found")
            return Response({"error": "Author not found"}, status=status.HTTP_404_NOT_FOUND)
        except ValueError as e:
            logger.warning(f"Validation error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CommentListCreateView(ListCreateAPIView):
    """
    API endpoint for listing all comments or creating a new comment.
    """
    queryset = Comment.objects.select_related('author', 'post').all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
