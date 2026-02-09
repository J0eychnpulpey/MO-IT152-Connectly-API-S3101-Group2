class PostFactory:
    @staticmethod
    def create_post(post_type, title, content, author, metadata=None):
        # ensure metadata is a dictionary
        if metadata is None:
            metadata = {}

        if post_type == 'image':
            # check if file_size is missing or empty
            if 'file_size' not in metadata or not metadata['file_size']:
                raise ValueError("Image posts require file_size in metadata.")
        
        if post_type == 'video':
            # check if duration is missing or empty
            if 'duration' not in metadata or not metadata['duration']:
                raise ValueError("Video posts require duration in metadata.")
        
        return Post.objects.create(
            title=title,
            content=content,
            post_type=post_type,
            author=author,
            metadata=metadata
        )
