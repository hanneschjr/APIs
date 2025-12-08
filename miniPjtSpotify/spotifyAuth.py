# API DE DADOS DE CLIMA DA OPENWEATHER - ENDPOINT: http://api.openweather.org/data/2.5/weather

import os
import dotenv
from request_api_utils import do_request
from requests.auth import HTTPBasicAuth
from pprint import pprint
import time

dotenv.load_dotenv()
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']

token_info = {
    "access_token": None,
    "expires_at": 0
}



def getSpotifyToken():
    global token_info

    if token_info['access_token']


    # Classe HTTPBasicAuth para geração do token em base64
    url = "https://accounts.spotify.com/api/token"
    auth = HTTPBasicAuth(username=client_id, password=client_secret)
    body = {
        "grant_type" : "client_credentials"
    }
    response = do_request(url, body, auth)
    pprint(response['expires_in'])
    if response

    # pprint(response)
    return response

if __name__ == "__main__":
    getSpotifyToken()