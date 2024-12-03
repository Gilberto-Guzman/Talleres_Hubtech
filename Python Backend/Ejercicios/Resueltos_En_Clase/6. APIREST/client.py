import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_All_post(self):
        try:
            response = requests.get(f"{self.base_url}/posts")
            response_json = response.json()

            return response
        except requests.exceptions.RequestException as e:
            print(f"{e}")

    def get_posts_by_user(self, user_id):
        pass

    def create_post(self, title, body, user_id):
        pass