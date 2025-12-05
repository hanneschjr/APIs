# AQUIVO DE REQUEST PARA GET(URL, PARAMS)
import requests

def do_request(url, body, auth):
    response = requests.post(url=url, data=body, auth=auth) # auth já faz colocar nos headers

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        response = None
    else:
        response = response.json()

    return response