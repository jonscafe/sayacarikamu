from requests_html import HTMLSession

import streamlit as st

def medium(user_input):
    st.write('MEDIUM')
    st.write('=========================')
    session = HTMLSession()
    search_url = f'https://medium.com/search/users?q={user_input}'

    search_response = session.get(search_url)
    search_response.html.render(timeout=10)

    usernames = search_response.html.find('a.af[href*="/@"]')

    # unique username
    unique_usernames = set()
    for username in usernames:
        # read until "/" and "?"
        username_text = username.attrs['href'].split('/')[1].split('?')[0]
        unique_usernames.add(username_text) #unique username

    for username_text in unique_usernames:
        st.write(f'Username: {username_text}, Link: https://medium.com/{username_text}')

    st.write('=========================')


if __name__ == "__main__":
    medium()
