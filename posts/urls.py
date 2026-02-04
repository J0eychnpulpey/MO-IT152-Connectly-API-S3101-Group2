from django.urls import path
from .views import UserListCreateView, PostListCreateView, CommentListCreateView

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
]
