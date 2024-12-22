from posts import PATH_TO_POST_IN_JP, PostSerializer
from posts.services import PostService
from json_placeholder import JSONPlaceHolderAdapter
from comments.services import CommentService
from comments.serializers import CommentSerializer

json_placeholder_adapter = JSONPlaceHolderAdapter()
post_service = PostService(json_placeholder_adapter)

response_create_post = post_service.create_post(title="Mi primer Post", body="Este es mi primer post en la API", user_id="1001")
print(response_create_post)

comments_service = CommentService(json_placeholder_adapter)
comments = comments_service.get_all_comments()
comment_serializer = CommentSerializer()
comment_serializer(comments)
print(comment_serializer.data)






# response = post_service.get_all_posts()

# response = post_service.get_all_posts(ruta = PATH_TO_POST_IN_JP)

# serializer = PostSerializer()

# serializer(response)

# print(PATH_TO_POST_IN_JP)

# print(serializer.data)