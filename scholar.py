import streamlit as st
from requests_html import HTMLSession

def scholar(user_input):
    st.write('SCHOLAR')
    st.write('=========================')
    session = HTMLSession()
    search_url = f'https://scholar.google.com/citations?view_op=search_authors&mauthors={user_input}&hl=id&oi=ao'

    search_response = session.get(search_url)
    search_response.html.render(timeout=10)
    user_input_lower = user_input.lower()
    info_author = search_response.html.text.lower()

    if user_input_lower in info_author:
        index = info_author.find(user_input_lower)
        
        name_and_affiliation_line = info_author[index:].split('\n')[0].strip()

        if ' Afliasi: ' in name_and_affiliation_line:
            name_index = name_and_affiliation_line.find(' Afliasi: ')
            name = name_and_affiliation_line[:name_index].strip()
            st.write('Nama:', name)
        else:
            st.write('Nama:', name_and_affiliation_line)

        st.write('Link Scholar:', search_response.url)
    else:
        st.write(f'No information found for {user_input}')
    
    st.write('=========================')

    
if __name__ == "__main__":
    scholar()
