from client import APIClient

client = APIClient("https://jsonplaceholder.typicode.com")

response = client.get_All_post()

print(response)