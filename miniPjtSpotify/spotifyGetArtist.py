# API  - ENDPOINT: https://api.spotify.com/v1/artists/{id}

import os
import dotenv
import requests

dotenv.load_dotenv()
token = os.environ['API_PASSWORD']

def getArtirstID(artistName):
    url = f"https://api.spotify.com/v1/artists/{artistName}"
    params = {
        'q': local,
        'appid': token,
        'units': 'metric',
        'lang': 'pt_br'
    }

    response = do_request(url=url, params=params)

    return response