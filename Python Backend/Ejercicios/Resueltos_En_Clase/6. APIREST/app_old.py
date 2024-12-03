import requests

try:
    # url = "https://jsonplaceholder.typicode.com/posts"
    url = "https://jsonplaceholder.typicode.com/postsloop"

    response = requests.get(url)
    print(response.status_code)

    response_json = response.json()
    # print(response_json)
    print(response_json[0]["title"])

# except Exception as e:
#     print(f'Hubo un problema {e}')
except KeyError as e:
    print(f'Hubo un problema al acceder a la key: {e}')