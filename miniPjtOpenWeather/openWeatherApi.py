import os
import dotenv
from request_api_utils import do_request
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

    response = do_request(url=url, params=params)

    return response