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
    body = {
        "grant_type" : "client_credentials"
    }
    response = request_token(url, body, auth)
    token_info['access_token'] = response['access_token']
    token_info['expires_at'] = time.time() + response["expires_in"] - 5


    return token_info['access_token']

if __name__ == "__main__":
    response = getSpotifyToken()
    pprint(response)