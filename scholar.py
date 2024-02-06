import streamlit as st
import requests
from bs4 import BeautifulSoup

def scholar(user_input):
    st.write('SCHOLAR')
    st.write('=========================')
    
    search_url = f'https://scholar.google.com/citations?view_op=search_authors&mauthors={user_input}&hl=id&oi=ao'
    search_response = requests.get(search_url)
    soup = BeautifulSoup(search_response.content, 'html.parser')

    author_info = soup.find('div', {'id': 'gsc_prf'})

    if author_info:
        name = author_info.find('div', {'id': 'gsc_prf_in'}).text.strip()
        affiliation = author_info.find('div', {'class': 'gsc_prf_il'}).text.strip()
        st.write('Nama:', name)
        st.write('Afliasi:', affiliation)
        st.write('Link Scholar:', search_url)
    else:
        st.write(f'Tidak ditemukan informasi untuk {user_input}')
    
    st.write('=========================')

if __name__ == "__main__":
    scholar()
