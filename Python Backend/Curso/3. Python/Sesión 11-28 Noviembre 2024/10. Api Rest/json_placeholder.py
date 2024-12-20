import requests

class JSONPlaceHolderAdapter:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def get_all_posts(self, ruta):
        try:
            response = requests.get(f"{self.base_url}/{ruta}")
            response_json = response.json()
            return response_json
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener las publicaciones: {e}")
            return []