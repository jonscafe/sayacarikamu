import streamlit as st
import requests
from bs4 import BeautifulSoup

def pddikti(user_input):
    st.write('PDDIKTI')
    st.write('=========================')
    search_url = f'https://pddikti.kemdikbud.go.id/search/{user_input}'

    search_response = requests.get(search_url)
    soup = BeautifulSoup(search_response.content, 'html.parser')

    mahasiswa_links = soup.find_all('a', href=lambda href: href and href.startswith('/data_mahasiswa/'))

    for link in mahasiswa_links[:5]:
        link_url = f"https://pddikti.kemdikbud.go.id{link['href']}"
        link_response = requests.get(link_url)
        link_soup = BeautifulSoup(link_response.content, 'html.parser')
        link_html_lower = link_soup.text.lower()
        if user_input.lower() in link_html_lower:
            st.write(f'{user_input}, PDDIKTI Mahasiswa: {link_url}')
    
    dosen_links = soup.find_all('a', href=lambda href: href and href.startswith('/data_dosen/'))
    for link in dosen_links[:5]:
        link_url = f"https://pddikti.kemdikbud.go.id{link['href']}"
        link_response = requests.get(link_url)
        link_soup = BeautifulSoup(link_response.content, 'html.parser')
        link_html_lower = link_soup.text.lower()
        if user_input.lower() in link_html_lower:
            st.write(f'{user_input}, PDDIKTI Dosen: {link_url}')
    
    st.write('=========================')

if __name__ == "__main__":
    pddikti()
