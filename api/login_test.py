import requests

result = requests.get('https://swapi.dev/api//planets/3')

print(result.text)
