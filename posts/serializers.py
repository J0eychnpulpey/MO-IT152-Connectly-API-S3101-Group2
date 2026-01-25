from rest_framework import serializers
from .models import User, Post, Comment


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model with validation and relational integrity."""
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'created_at', 'is_verified']
        read_only_fields = ['id', 'created_at']
    
    def validate_username(self, value):
        """Ensure username is not empty and has minimum length."""
        if not value or not value.strip():
            raise serializers.ValidationError("Username cannot be empty.")
        if len(value.strip()) < 1:
            raise serializers.ValidationError("Username must be at least 1 character.")
        return value.strip()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model with author relationship validation."""
    comments = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'content', 'author', 'created_at', 'is_published', 'comments']
        read_only_fields = ['id', 'created_at', 'comments']
    
    def get_comments(self, obj):
        """Return list of comment IDs for this post."""
        return list(obj.comments.values_list('id', flat=True))
    
    def validate_content(self, value):
        """Ensure content is not empty."""
        if not value or not value.strip():
            raise serializers.ValidationError("Content cannot be empty.")
        return value.strip()
    
    def validate_author(self, value):
        """Ensure author exists."""
        if not value:
            raise serializers.ValidationError("Author is required.")
        return value


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model with post and author relationship validation."""
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'author', 'post', 'created_at']
        read_only_fields = ['id', 'created_at']
    
    def validate_text(self, value):
        """Ensure text is not empty."""
        if not value or not value.strip():
            raise serializers.ValidationError("Text cannot be empty.")
        return value.strip()
    
    def validate_post(self, value):
        """Ensure post exists."""
        if not value:
            raise serializers.ValidationError("Post is required.")
        return value
    
    def validate_author(self, value):
        """Ensure author exists."""
        if not value:
            raise serializers.ValidationError("Author is required.")
        return value
