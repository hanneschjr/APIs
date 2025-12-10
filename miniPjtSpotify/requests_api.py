# REQUEST PARA TOKEN, NAME_ID, 
import requests

def request_token(url, body, auth):
    response = requests.post(url=url, data=body, auth=auth) # auth já faz colocar nos headers

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        response = None
    else:
        response = response.json()

    return response

def request_artist(url, params, token):
    headers ={
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=url, params=params, headers=headers)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        response = None
    else:
        response = response.json()

    return response

def request_top_muisics(url, token):
    headers ={
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url=url, headers=headers)

    try:
        response.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        response = None
    else:
        response = response.json()

    return response