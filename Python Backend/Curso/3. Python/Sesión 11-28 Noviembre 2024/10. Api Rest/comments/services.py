from .models import Comment
import requests


class CommentService:
    def __init__(self, json_placeholder_adapter):
        self.json_place_holder_service = json_placeholder_adapter

    def get_all_comments(self):
        try:
            response_json = self.json_place_holder_service.get_all_comments()
            return [Comment.from_dict(comment) for comment in response_json]
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []
    
    def create_comments(self):
        pass

    def get_all_comments_by_post(self):
        pass