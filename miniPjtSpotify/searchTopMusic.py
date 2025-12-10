# API SPOTIFY PARA OBTER AS PRINCIPAIS MÚSICAS DE UM ARTISTA - ENDPOINT: http://api.openweather.org/data/2.5/weather
from requests_api import request_top_muisics
from getToken import getSpotifyToken
from pprint import pprint

def getTopMusics(id_artist):
    url = f"https://api.spotify.com/v1/artists/{id_artist}/top-tracks"
    token = getSpotifyToken()
    response = request_top_muisics(url, token)

    return response

if __name__ == "__main__":
    response = getTopMusics("246dkjvS1zLTtiykXe5h60")
    pprint(response)