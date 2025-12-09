# API DE DADOS DE CLIMA DA OPENWEATHER - ENDPOINT: http://api.openweather.org/data/2.5/weather

import os
import dotenv
from miniPjtSpotify.requests_api import request_item
import requests

dotenv.load_dotenv()
token = os.environ['API_PASSWORD']

def openWeatherApi(local):
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': local,
        'appid': token,
        'units': 'metric',
        'lang': 'pt_br'
    }

    response = request_item(url=url, params=params)

    return response