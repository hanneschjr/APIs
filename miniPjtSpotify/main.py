# FRONT-END EM STREAMLIT WEB APP SPOTIFY
import streamlit as st
import pandas as pd
import streamlit as st
from getToken import getSpotifyToken
from searchArtist import getArtist
from searchTopMusic import getTopMusics

def main():
    st.title("Web App Spotify")
    st.write('Dados da API do Spotify: (https://developer.spotify.com/documentatioon/web-api)')
    nome_artista = st.text_input('Busque um artista:')

    if not nome_artista:
        st.warning(f"Dados não encontrados para o nome: {nome_artista}")
        st.stop()
    
    artista = getArtist(nome_artista)

    if not artista:
        st.warning(f'Artista não foi encontrado! (busca: {nome_artista})')

    id_artista = artista['id']
    nome_artista = artista['name']
    popularidade_artista = artista['popularity']

    melhores_musicas = getTopMusics(id_artista)

    st.subheader(f'Artista: {nome_artista} (pop: {popularidade_artista})')
   
    for musica in melhores_musicas['tracks']:
        nome_musica = musica['name']
        popularidade_musica = musica['popularity']
        st.write(f'{nome_musica} (pop: {popularidade_musica})')
    


if __name__ == '__main__':
    main()