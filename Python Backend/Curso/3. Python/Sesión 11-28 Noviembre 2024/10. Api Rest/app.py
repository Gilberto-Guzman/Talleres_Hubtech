from client import APIClient
from posts import PATH_TO_POST_IN_JP, PostSerializer
from posts.services import PostService
from json_placeholder import JSONPlaceHolderAdapter

json_placeholder_adapter = JSONPlaceHolderAdapter()
post_service = PostService(json_placeholder_adapter)

response = post_service.get_all_posts()

# response = post_service.get_all_posts(ruta = PATH_TO_POST_IN_JP)

serializer = PostSerializer()

serializer(response)

# print(PATH_TO_POST_IN_JP)

print(serializer.data)
