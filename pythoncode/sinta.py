import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

def sinta(user_input):
    print('SINTA AUTHOR')
    print('=========================')
    session = HTMLSession()
    search_url = f'https://sinta.kemdikbud.go.id/authors/?q={user_input}'

    search_response = session.get(search_url)
    search_response.html.render(timeout=10)

    # Extract links that contain '/authors/profile/'
    profile_links = search_response.html.find('a[href*="/authors/profile/"]')

    if not profile_links:
        print('Tidak ditemukan!')
    else:
        for profile_link in profile_links:
            # Extracting name from the opened link
            profile_response = requests.get(profile_link.absolute_links.pop())
            profile_soup = BeautifulSoup(profile_response.content, 'html.parser')
            name_element = profile_soup.find('h3').find('a')
            name = name_element.text.strip() if name_element else 'Tidak ditemukan!'

            print(f'Name: {name}, Link: {profile_link.absolute_links.pop()}')

    print('=========================')

if __name__ == "__main__":
    user_input = input("Input Name: ")
    sinta(user_input)
