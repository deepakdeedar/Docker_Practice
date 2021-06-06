import requests

response = requests.get('https://swapi.dev/api/films/')
data = response.json()
print(data)