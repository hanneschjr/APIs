# AQUIVO DE REQUEST PARA GET(URL, PARAMS)

import requests

def do_request(url, params=None):
    response = requests.get(url, params)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        response = None
    else:
        response = response.json()

    return response