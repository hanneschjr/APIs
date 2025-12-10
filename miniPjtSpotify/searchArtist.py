# API  SEARCH ITEM- ENDPOINT: https://api.spotify.com/v1/search

from requests_api import request_artist
from getToken import getSpotifyToken
from pprint import pprint


# def getItem(item, type):
#     url = "https://api.spotify.com/v1/search"
#     params = {
#         'q': item,
#         'type': type,
#     }

def getArtist(artista):
    url = "https://api.spotify.com/v1/search"
    params = {
        "q": artista,
        "type": "artist",
    }
    token = getSpotifyToken()
    response = request_artist(url, params, token)
    try:
        primeiro_resultado = response['artists']['items'][0]
    except IndexError:
        primeiro_resultado = None
    return primeiro_resultado

if __name__ == "__main__":
    response = getArtist("Post Malone")
    pprint(response)