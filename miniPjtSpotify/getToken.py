# API PARA OBTER O TOKEN DE AUTENTICAÇÃO DO SPOTIFY - ENDPOINT: https://accounts.spotify.com/api/token
import os
import dotenv
from requests_api import request_token
from requests.auth import HTTPBasicAuth
from pprint import pprint
import time
from tokenStore import token_info


def getSpotifyToken():
    dotenv.load_dotenv()
    client_id = os.environ['SPOTIFY_CLIENT_ID']
    client_secret = os.environ['SPOTIFY_CLIENT_SECRET']


    # condições que envolvem que o token está válido
    if token_info['access_token'] and token_info['expires_at'] > time.time():
        return token_info['access_token']

    # Classe HTTPBasicAuth para geração do token em base64
    url = "https://accounts.spotify.com/api/token"
    auth = HTTPBasicAuth(username=client_id, password=client_secret)
    # Alternativamente ao uso da biblioteca HTTPBasicAuth:
    # auth_string = f'{client_id}:{client_secret}'.encode() # transforma em byte pois a função base64.b64encode() só aceita o formanto bytes
    # auth_string = base64.b64encode(auth_string) # codifica o binário em base 64
    # auth_string = auth_string.decode() # retorna o byte para string novamente 
    # Obs.: O método HTTPBasicAuth() é um método que age como uma instrução ao request de que você deseja fazer uma autenticação basic
    # É o request que recebe usuário e senha e a instrução que faz todas as tarefas acima além de montar e inserir no header da requisição!

    # parâmetro obrigatório na API do Spotify
    body = {
        "grant_type" : "client_credentials"
    }
    response = request_token(url, body, auth)
    token_info['access_token'] = response['access_token']
    token_info['expires_at'] = time.time() + response["expires_in"] - 5


    return token_info['access_token']

if __name__ == "__main__":
    response = getSpotifyToken()
