# API  SEARCH ITEM- ENDPOINT: https://api.spotify.com/v1/search
import os
import dotenv
import requests
from miniPjtSpotify.requests import request_item
from getToken import getSpotifyToken
from pprint import pprint

dotenv.load_dotenv()
token = os.environ['API_PASSWORD']

def getItem(item, type):
    url = "https://api.spotify.com/v1/search"
    params = {
        'q': item,
        'type': type,
    }
    token = getSpotifyToken()
    response = request_item(url, params, token)

    return response

if "__mai__" == __name__:
    response = getItem("Cristiano Araújo", "artist")
    pprint(response)