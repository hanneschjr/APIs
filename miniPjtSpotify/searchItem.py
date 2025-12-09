# API  SEARCH ITEM- ENDPOINT: https://api.spotify.com/v1/search

from requests_api import request_item
from getToken import getSpotifyToken
from pprint import pprint


# def getItem(item, type):
#     url = "https://api.spotify.com/v1/search"
#     params = {
#         'q': item,
#         'type': type,
#     }

def getItem(item, type):
    url = "https://api.spotify.com/v1/search"
    params = {
        "q": item,
        "type": type,
    }
    token = getSpotifyToken()
    response = request_item(url, params, token)

    return response

if __name__ == "__main__":
    response = getItem("Post Malone", "artist")
    pprint(response)