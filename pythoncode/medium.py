from requests_html import HTMLSession

def medium(user_input):
    print('MEDIUM')
    print('=========================')
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
        print(f'Username: {username_text}, Link: https://medium.com/{username_text}')

    print('=========================')

if __name__ == "__main__":
    medium()
