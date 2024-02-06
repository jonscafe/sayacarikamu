import streamlit as st
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def datadikti(user_input):
    st.write('DATADIKTI')
    st.write('=========================')
    session = HTMLSession()
    input_lower = user_input.lower()
    formatted_input = input_lower.replace(" ", "-")

    search_url = f'https://www.datadikti.com/searches/{formatted_input}'
    search_response = session.get(search_url)
    
    soup = BeautifulSoup(search_response.text, 'html.parser')

    data_mahasiswa = soup.find_all('li')

    for item in data_mahasiswa:
        st.write(item.text)
    
    st.write('=========================')

if __name__ == "__main__":
    datadikti()
