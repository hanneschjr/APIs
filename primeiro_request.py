import requests
import pprint

url = 'https://httpbin.org/get'

resposta = requests.get(url)

print(resposta.json())