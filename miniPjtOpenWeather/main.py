# FRONT-END EM STREAMLIT 

import pandas as pd
import streamlit as st
from openWeatherApi import openWeatherApi


def main():
    st.title("Web App Tempo")
    st.write('Dados do OpenWeather: (https://openweathermap.org/current)')
    local = st.text_input('Digite uma cidade:')
    dados_tempo = openWeatherApi(local)

    if not dados_tempo:
        st.warning(f"Dados não encontrados para a cidade {local}")
        st.stop()
    
    clima_atual = dados_tempo['weather'][0]['description']
    temperatura = dados_tempo['main']['temp']
    sensacao_termica = dados_tempo['main']['feels_like']
    umidade = dados_tempo['main']['humidity']
    cobertura_nuves = dados_tempo['clouds']['all']
    
    st.metric(label='Tempo atual', value=clima_atual)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Teperatura", value=f'{temperatura} °C')
        st.metric(label="Sensação Térmica", value=f'{sensacao_termica} °C')
    with col2:
        st.metric(label="Umidade", value=f'{umidade} %')
        st.metric(label="Cobertura de Nuvens", value=f'{cobertura_nuves} %')


if __name__ == '__main__':
    main()