import requests
from pprint import pprint
import random
import os
import json

######### GET ##############
def consulta(): 
    url = 'https://httpbin.org/get'
    resposta = requests.get(url)
    pprint.pprint(resposta.json())

########## POST #############
def envio_form():
    url = 'https://httpbin.org/post'
    data = {
        "meus_dados": [1,2,3],
        "pessoa":{
            "nome": "Juliano",
            "professor": True
        }
    }
    params = { 
        "dataInicio": "2025-11-06",
        "dataFim": "2025-11-17"
    }
    resposta = requests.post(url, json=data, params=params)
    pprint.pprint(resposta.json())
    print('#### URL:')
    pprint.pprint(resposta.request.url)


########### API IBGE ###############

def api_ibge_nomes():
    nome = 'darci'
    url = f"https://servicodados.ibge.gov.br/api/v2/censos/nomes/{nome}"

    params = {
        "sexo": "M",
        "groupBy": "UF",
    }

    resposta = requests.get(url, params=params)

    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resultado = None
    else:
        resultado = resposta.json()
        # pprint(resultado)
        with open('resposta.json') as f:
            json.dump(resultado, f, indent=2)



def auth_matomo():
    url = "https://matomo-cds.eb.mil.br/index.php"
    # params = {
    #     "segment": "eventCategory==V%25C3%25ADdeos",
    #     "module": "Live",
    #     "action": "getLastVisitsDatails",
    #     "idSite": 36,
    #     "small": 1,
    #     "period": "day",
    #     "showtitle": 1,
    #     "random": random.randint(1, 9999),
    #     "viewDataTable": "VisitorLog",
    #     "date": "yesterday",
    #     "format": "JSON",
    #     "forceView": 1,
    #     "token_auth": "faaa918d51c907b9ac43c63e77a13c5e",
    #     "filter_limit": 5
    # }

    params = {
    "module": "API",
    "method": "Live.getLastVisitsDetails",
    "idSite": "36",
    # "period": "range",  
    "period": "day",  
    # "date": "last30",
    # "date": "today",
    "date": "last365",
    # "lastMinutes": "30",
    "format": "JSON",
    "token_auth": "faaa918d51c907b9ac43c63e77a13c5e",
    "filter_limit":-1
    }

    resposta = requests.get(url, params=params)
    try:
        resposta.raise_for_status()
    except requests.HTTPError as e:
        print(f'Erro no request: {e}')
        resultado = None
    # except requests.ConnectTimeout as e:
    #     print(f'Erro timeout: {e}')
    #     resultado = None
    else:
        print("executei este código")
        resultado = resposta.json()
        pprint(resposta.request.url)
        with open('resposta.json', 'w') as f:
            json.dump(resultado, f, indent=2)

if __name__ == "__main__":
    api_ibge_nomes()